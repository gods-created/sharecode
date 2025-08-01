from .models import Room
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now, timedelta
from loguru import logger

@receiver(pre_save, sender=Room)
def deleting_oldest_rooms(instance: Room, *args, **kwargs) -> None:
    boundary = now() - timedelta(days=3)
    deleted, _ = Room.objects.filter(updated_at__lte=boundary).delete()
    logger.debug(f'Deleted {deleted} rooms.')
    return None