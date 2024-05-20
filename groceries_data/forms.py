from django.forms import ModelForm, TextInput, NumberInput
from groceries_data.models import GroceriesInfo
from bootstrap_datepicker_plus.widgets import DatePickerInput

class GroceriesInfoForm(ModelForm):
    class Meta:
        model = GroceriesInfo
        exclude = ["uploader"]
        widgets = {
            "product_name": TextInput(attrs={"placeholder": "Name of the Product/Produce/Goods"}),
            "quantity": NumberInput(attrs={"placeholder": "How many of the Product/Produce/Goods did you purchase?"}),
            "size": NumberInput(attrs={"placeholder": "Size/Weight of the Product/Produce/Goods"}),
            "money_spent": NumberInput(attrs={"placeholder": "How much was spent on the Product/Produce/Goods"}),
            "purchase_date": DatePickerInput(options={"format": "DD/MM/YYYY"}),
            "store_name": TextInput(attrs={"placeholder": "Name of Store"}),
            "location": TextInput(attrs={"placeholder": "Where is the store located?"}),
        }