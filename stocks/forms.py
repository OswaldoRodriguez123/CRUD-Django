from django import forms
from django.forms import ModelForm

from .models import Stocks

class DateInput(forms.DateInput):
    input_type = 'date'

class StocksForm(ModelForm):
    class Meta:
        model = Stocks
        fields = "__all__"
        widgets = {
            'stock_vence': DateInput()
        }
