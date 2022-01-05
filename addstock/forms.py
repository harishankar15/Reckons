from django import forms
from .models import addstockModel

class addstockForm(forms.ModelForm):
    class Meta():
        model = addstockModel
        fields = '__all__'

