# hotel_booking/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.available_rooms, name='available_rooms'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('booking_success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('add-room/', views.add_room, name='add_room'),
    path('room/<int:room_id>/', views.room_details, name='room_details'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('manage_rooms/', views.manage_rooms, name='manage_rooms'),
    path('edit_room/<int:id>/', views.edit_room, name='edit_room'),
    path('delete_room/<int:id>/', views.delete_room, name='delete_room'),  # Add this line for delete_room
    path('add/', views.add_room, name='add_room'),
    path('edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('bookings/approve/<int:booking_id>/', views.approve_booking, name='approve_booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

