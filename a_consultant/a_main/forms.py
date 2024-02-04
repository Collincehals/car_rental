from django.forms import ModelForm
from django import forms
from .models import *

class CarPostForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', 'id']
        
        labels = {
            'name': 'Name',
            'hire_rate_hour': 'Rate/Hour',
            'hire_rate_day': 'Rate/Day',
            'image': 'Upload Image',
        }
        
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
            'brand' : forms.CheckboxSelectMultiple()
        }

class TripBookingForm(ModelForm):
    class Meta:
        model = TripBooking
        exclude = ['user', 'booking_number', ]
        
        widgets = {
            'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
            'drop_off_date': forms.DateInput(attrs={'type': 'date'}),
           'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class CarRentalForm(ModelForm):
    class Meta:
        model = CarRental
        exclude = ['customer', 'renting_id','status','car',]
        
        widgets = {
            'rental_start_date': forms.DateInput(attrs={'type': 'date'}),
            'rental_end_date': forms.DateInput(attrs={'type': 'date'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
        }