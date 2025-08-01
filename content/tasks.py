from celery import shared_task
from .models import Content
from room.models import Room

@shared_task(bind=True, queue='high_priority')
def write_content(self, room_number: int, code: str = '', output: str = '') -> None:
    try:
        if (obj := Content.objects.filter(room__number=room_number).first()) is not None:
            obj.code = code if code else obj.code
            obj.output = output if output else obj.output
            obj.save()
            return
        
        room = Room.objects.filter(number=room_number).first()
        obj = Content.objects.create(
            room=room,
            code=code,
            output=output
        )

        return

    except (Exception, ) as e:
        self.retry(exc=str(e), max_retries=3, countdown=5)