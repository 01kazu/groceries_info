# Generated by Django 4.2.13 on 2024-05-19 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_data', '0007_groceriesinfo_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceriesinfo',
            name='store_owner_name',
        ),
    ]