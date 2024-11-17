
from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'check_in_date', 'check_out_date']
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'price']