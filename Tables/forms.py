# forms.py

from django import forms
from .models import foodcat

class FoodCatForm(forms.ModelForm):
    class Meta:
        model = foodcat
        fields = ['catImage', 'cat_id', 'catname', 'Description', 'number_items']
