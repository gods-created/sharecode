from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError
)
from .models import Room
from django.forms.models import model_to_dict
from enums import Languages

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = 'number', 'language',
        read_only_fields = 'number',
    
    language = CharField(
        required=True,
        allow_blank=False,
    )

    def validate_language(self, language):
        if language not in [item.value for item in Languages]:
            raise ValidationError('Incorrect programming language.')
        
        return language

    def create_room(self) -> dict:
        language = self.validated_data.get('language')
        obj = Room.objects.create_room(language=language)
        return model_to_dict(obj)