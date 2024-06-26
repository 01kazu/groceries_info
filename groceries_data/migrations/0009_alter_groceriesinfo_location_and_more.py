# Generated by Django 4.2.13 on 2024-05-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_data', '0008_remove_groceriesinfo_store_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceriesinfo',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='groceriesinfo',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='groceriesinfo',
            name='store_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='groceriesinfo',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'Kilograms (KG)'), ('g', 'Grams (g)'), ('oz', 'Ounces (oz)'), ('lb', 'Pounds (lb)'), ('ml', 'Milliliters (mL)'), ('cl', 'Centiliters (cL)'), ('l', 'Liters (L)'), ('pt', 'Pint (pt)'), ('fl oz', 'Fluid Ounces (fl oz)'), ('qt', 'Quarts (qt)'), ('gal', 'Gallon (gal)')], max_length=10, null=True),
        ),
    ]
