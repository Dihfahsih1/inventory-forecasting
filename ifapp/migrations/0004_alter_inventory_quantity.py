# Generated by Django 4.2 on 2023-04-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifapp', '0003_alter_inventory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
