from django.db import models

class Inventory(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    quantity_used = models.IntegerField()
    remaining_stock = models.IntegerField()
    # other fields as needed
    
    def __str__(self):
        return f'{self.item_name} - {self.quantity} on {self.date}'
