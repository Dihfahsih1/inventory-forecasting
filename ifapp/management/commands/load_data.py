from django.core.management.base import CommandError, BaseCommand
from ifapp.models import Inventory

class Command(BaseCommand):
    help = 'Load sample inventory data into the database'

    def handle(self, *args, **options):
        # Generate sample data or read it in from a file
        data = [   
             {'date': '2022-01-01', 'item_name': 'Item A', 'quantity': 100, 'quantity_used': 10, 'remaining_stock': 90},    {'date': '2022-01-02', 'item_name': 'Item A', 'quantity': 90, 'quantity_used': 20, 'remaining_stock': 70},    {'date': '2022-01-03', 'item_name': 'Item A', 'quantity': 65, 'quantity_used': 5, 'remaining_stock': 65},    {'date': '2022-01-01', 'item_name': 'Item B', 'quantity': 100, 'quantity_used': 15, 'remaining_stock': 85},    {'date': '2022-01-02', 'item_name': 'Item B', 'quantity': 85, 'quantity_used': 10, 'remaining_stock': 75},    {'date': '2022-01-03', 'item_name': 'Item B', 'quantity': 75, 'quantity_used': 25, 'remaining_stock': 50},    {'date': '2022-01-04', 'item_name': 'Item A', 'quantity': 65, 'quantity_used': 15, 'remaining_stock': 50},    {'date': '2022-01-04', 'item_name': 'Item B', 'quantity': 50, 'quantity_used': 20, 'remaining_stock': 30},    {'date': '2022-01-05', 'item_name': 'Item A', 'quantity': 50, 'quantity_used': 10, 'remaining_stock': 40},    {'date': '2022-01-05', 'item_name': 'Item B', 'quantity': 30, 'quantity_used': 15, 'remaining_stock': 15},]


        # Save the data to the database
        for item in data:
            inventory_item = Inventory(
                date=item['date'],
                item_name=item['item_name'],
                quantity_used=item['quantity_used'],
                remaining_stock=item['remaining_stock']
            )
            inventory_item.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded inventory data'))
