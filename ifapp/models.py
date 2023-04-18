from django.db import models

class Inventory(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(blank=True, null=True)
    quantity_used = models.IntegerField(default=0, blank=True, null=True)
    remaining_stock = models.IntegerField(default=0, blank=True, null=True)
    # other fields as needed
    
    def __str__(self):
        return f'{self.item_name} - {self.quantity} on {self.date}'
