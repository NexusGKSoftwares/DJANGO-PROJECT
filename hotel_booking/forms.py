from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'check_in_date', 'check_out_date']


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'price', 'image']
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'price', 'image']

class BookingApprovalForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['approved']