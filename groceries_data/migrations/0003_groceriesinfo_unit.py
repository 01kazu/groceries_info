# Generated by Django 4.2.13 on 2024-05-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_data', '0002_alter_groceriesinfo_money_spent'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceriesinfo',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'Kilograms (KG)'), ('g', 'Grams (g)'), ('oz', 'Ounces (oz)'), ('lb', 'Pounds (lb)'), ('ml', 'Milliliters (mL)'), ('cl', 'Centiliters (cL)'), ('l', 'Liters (L)'), ('pt', 'Pint (pt)'), ('fl oz', 'Fluid Ounces (fl oz)'), ('qt', 'Quarts (qt)'), ('gal', 'Gallon (gal)')], max_length=10),
        ),
    ]