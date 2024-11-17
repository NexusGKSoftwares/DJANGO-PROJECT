# hotel_booking/views.py
from django.shortcuts import render, get_object_or_404, redirect

from .models import Room, Booking
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'hotel_booking/index.html')

def add_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']

        # Save the room information in the database
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        room_url = fs.url(filename)

        room = Room.objects.create(
            name=name,
            description=description,
            price=price,
            image=room_url
        )
        
        return redirect('available_rooms')  # Redirect to available rooms page after successful submission
    
    return render(request, 'hotel_booking/add_room.html')

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
