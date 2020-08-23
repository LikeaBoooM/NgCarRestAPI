from django import forms
from . models import Car, Rate

class NewCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['mark', 'model',]

class NewRateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = ['grade',]