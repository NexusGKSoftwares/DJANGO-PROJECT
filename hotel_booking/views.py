# hotel_booking/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Room, Booking
from .forms import BookingForm

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
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'hotel_booking/book_room.html', {'form': form, 'room': room})
