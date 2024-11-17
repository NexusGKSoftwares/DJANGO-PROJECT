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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
