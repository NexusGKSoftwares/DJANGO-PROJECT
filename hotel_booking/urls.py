# hotel_booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.available_rooms, name='available_rooms'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
]
