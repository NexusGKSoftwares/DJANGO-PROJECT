# hotel_booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from .forms import BookingForm


def index(request):
    return render(request, 'hotel_booking/index.html')
def available_rooms(request):
    rooms = Room.objects.filter(availability=True)
    return render(request, 'hotel_booking/available_rooms.html', {'rooms': rooms})

def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.total_price = room.price_per_night * (booking.check_out_date - booking.check_in_date).days
            booking.save()
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'hotel_booking/book_room.html', {'form': form, 'room': room})

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'hotel_booking/booking_success.html', {'booking': booking})
