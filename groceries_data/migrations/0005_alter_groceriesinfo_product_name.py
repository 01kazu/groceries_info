# Generated by Django 4.2.13 on 2024-05-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_data', '0004_alter_groceriesinfo_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceriesinfo',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
    ]
