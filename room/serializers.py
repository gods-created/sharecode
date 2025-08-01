from rest_framework.serializers import (
    ModelSerializer,
)
from .models import Room
from django.forms.models import model_to_dict

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = 'number',
        read_only_fields = 'number',

    def create_room(self) -> dict:
        obj = Room.objects.create_room()
        return model_to_dict(obj)