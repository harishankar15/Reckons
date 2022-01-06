from django import forms
from .models import addproductModel

class addproductForm(forms.ModelForm):
    class Meta():
        model = addproductModel
        fields = '__all__'

