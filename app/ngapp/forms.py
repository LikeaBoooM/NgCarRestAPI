from django import forms
from . models import Car

class NewCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['mark', 'model',]