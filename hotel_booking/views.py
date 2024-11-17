from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room, Booking
from .forms import AddRoomForm, BookingApprovalForm, RoomForm  # Import the AddRoomForm

def index(request):
    rooms = Room.objects.all()  # Fetch all rooms from the database
    return render(request, 'hotel_booking/index.html', {'rooms': rooms})
def add_room(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Automatically saves the room data, including the image
            messages.success(request, 'Room added successfully!')
            return redirect('available_rooms')  # Redirect to the available rooms page after successful submission
        else:
            # If the form is invalid, render the form with error messages
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddRoomForm()  # Empty form for GET request

    return render(request, 'hotel_booking/add_room.html', {'form': form})

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
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'hotel_booking/booking_success.html', {'booking': booking})
def room_details(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'hotel_booking/room_details.html', {'room': room})
# Admin View: Add Room
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin:manage_rooms')  # Redirect to the room list page
    else:
        form = RoomForm()
    return render(request, 'admin/add_room.html', {'form': form})

# Admin View: Edit Room
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('admin:manage_rooms')  # Redirect to the room list page
    else:
        form = RoomForm(instance=room)
    return render(request, 'admin/edit_room.html', {'form': form, 'room': room})

# Admin View: Manage All Rooms
def manage_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'admin/manage_rooms.html', {'rooms': rooms})

# Admin View: Approve or Reject Booking
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        form = BookingApprovalForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('admin:view_bookings')  # Redirect to the bookings list
    else:
        form = BookingApprovalForm(instance=booking)
    
    return render(request, 'admin/approve_booking.html', {'booking': booking, 'form': form})

# Admin View: View All Bookings
def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'admin/view_bookings.html', {'bookings': bookings})