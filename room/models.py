from django.db.models import (
    Model,
    IntegerField,
    DateTimeField,
    Index
)
from .managers import RoomManager

class Room(Model):
    number = IntegerField(null=False, blank=False, unique=True)
    updated_at = DateTimeField(auto_now_add=True)
    objects = RoomManager()

    class Meta:
        app_label = 'room'
        db_table = 'rooms'
        ordering = ['pk', 'number', 'updated_at']
        indexes = (
            Index(fields=['number']),
            Index(fields=['updated_at']),
        )
    
    def __str__(self):
        return str(self.number)