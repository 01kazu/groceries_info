from django.db import models

# Create your models here.
class GroceriesInfo(models.Model):
    UNITS = [
        ("kg", "Kilograms (KG)"),
        ("g", "Grams (g)"),
        ("oz", "Ounces (oz)"),
        ("lb", "Pounds (lb)"),
        ("ml", "Milliliters (mL)"),
        ("cl", "Centiliters (cL)"),
        ("l",  "Liters (L)"),
        ("pt", "Pint (pt)"),
        ("fl oz", "Fluid Ounces (fl oz)"),
        ("qt", "Quarts (qt)"),
        ("gal", "Gallon (gal)"),
    ]
    product_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    size = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    unit = models.CharField(max_length=10, choices=UNITS, blank=True, null=True)
    money_spent = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_date = models.DateField()
    store_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.quantity: .1f} {self.product_name}s bought on {self.purchase_date: %d %B, %Y}'

