from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time', 'date']
        widgets = {'date': forms.DateInput(attrs={'id': 'datetimepicker12'})}
