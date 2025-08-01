from rest_framework.serializers import (
    ModelSerializer,
    IntegerField
)
from .models import Content
from django.forms.models import model_to_dict

class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = 'code', 'output', 'room_number'
        read_only_fields = 'code', 'output',
    
    room_number = IntegerField(required=True)

    def room_content(self) -> dict:
        room_number = self.validated_data.get('room_number')
        obj = Content.objects.filter(room__number=room_number).first()
        return model_to_dict(obj) if obj is not None else {}