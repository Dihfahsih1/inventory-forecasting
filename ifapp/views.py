from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm

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
