from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm
from prophet import Prophet
import pandas as pd
#import pdb; pdb.set_trace()

from django.conf import settings
model = Prophet(
    yearly_seasonality=settings.PROPHET_YEARLY_SEASONALITY,
    weekly_seasonality=settings.PROPHET_WEEKLY_SEASONALITY,
    daily_seasonality=settings.PROPHET_DAILY_SEASONALITY,
)

def inventory_forecast(request):
    # Load inventory data from the database
    inventory_queryset = Inventory.objects.all()

    # Convert inventory queryset to a pandas dataframe
    inventory_data = pd.DataFrame.from_records(inventory_queryset.values())

    # Convert date column to datetime format
    inventory_data['date'] = pd.to_datetime(inventory_data['date'])

    # Rename columns to fit Prophet requirements
    inventory_data = inventory_data.rename(columns={'date': 'ds', 'quantity': 'y'})

    # Train the Prophet model
    model = Prophet() 
    try:
        model.fit(inventory_data, mcmc_samples=1)
        print(model)
    except Exception as e:
        print("Error fitting model: ", e)

    # Generate forecast data for the next 30 days
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Get the last 30 days of actual inventory data
    actual = inventory_data.tail(30)

    # Combine forecast and actual data into a single dataframe
    forecast_data = forecast[['ds', 'yhat']].tail(30)
    forecast_data = forecast_data.rename(columns={'ds': 'date', 'yhat': 'quantity'})
    forecast_data['date'] = pd.to_datetime(forecast_data['date'])

    actual_data = actual.rename(columns={'ds': 'date'})

    inventory_data = pd.concat([actual_data, forecast_data], ignore_index=True)

    # Render the forecast page with the inventory data
    return render(request, 'inventory_forecast.html', {'inventory_data': inventory_data})

def inventory_list(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventory_items': inventory_items})

def inventory_detail(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory_detail.html', {'inventory_item': inventory_item})

def inventory_new(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.save()
            return redirect('inventory_detail', pk=inventory_item.pk)
    else:
        form = InventoryForm()
    return render(request, 'inventory_edit.html', {'form': form})
def inventory_delete(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)

    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')

    return render(request, 'inventory_delete.html', {'inventory_item': inventory_item})
def inventory_edit(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=inventory_item)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.save()
            return redirect('inventory_detail', pk=inventory_item.pk)
    else:
        form = InventoryForm(instance=inventory_item)
    return render(request, 'inventory_edit.html', {'form': form, 'inventory_item': inventory_item})
