# Generated by Django 4.2.13 on 2024-05-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_data', '0011_alter_groceriesinfo_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceriesinfo',
            name='money_spent',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]