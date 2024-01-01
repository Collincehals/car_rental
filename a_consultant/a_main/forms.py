from django.forms import ModelForm
from django import forms
from .models import *

class CarPostForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'hire_rate', 'image', 'description']
        
        labels = {
            'name': 'Name',
            'hire_rate': 'Rate',
            'image': 'Upload Image',
            'description': 'Specification',
        }
        
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
            'brand' : forms.CheckboxSelectMultiple()
        }