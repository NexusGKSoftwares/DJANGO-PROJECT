# hotel_booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'hotel_booking/index.html')

def available_rooms(request):
    rooms = Room.objects.all()  # Fetch all available rooms
    return render(request, 'hotel_booking/available_rooms.html', {'rooms': rooms})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        # Process booking form
        name = request.POST['name']
        email = request.POST['email']
        duration = int(request.POST['duration'])
        total_cost = room.price * duration

        # Create booking
        booking = Booking.objects.create(
            room=room,
            name=name,
            email=email,
            duration=duration,
            total_cost=total_cost
        )

        messages.success(request, 'Your booking was successful!')
        return redirect('booking_success', booking_id=booking.id)

    return render(request, 'hotel_booking/book_room.html', {'room': room})

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'hotel_booking/booking_success.html', {'booking': booking})
