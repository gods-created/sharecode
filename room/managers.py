from django.db.models import Manager
from random import choice
from string import digits

class RoomManager(Manager):
    def _number(self) -> str:
        return ''.join(choice(digits) for _ in range(9))

    def create_room(self):
        number = int(self._number())
        room = self.filter(number=number).first()
        if room:
            self.create_room()
        obj = self.create(number=number)
        return obj