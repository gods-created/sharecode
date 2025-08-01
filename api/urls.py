from django.urls import path
from room.views import create_room, room_content

app_name = 'api'

urlpatterns = [
    path('create_room/', create_room, name='create_room'),
    path('room_content/', room_content, name='room_content')
]