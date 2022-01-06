from django import forms
from .models import adduserModel

class adduserForm(forms.ModelForm):
    class Meta():
        model = adduserModel
        fields = '__all__'

