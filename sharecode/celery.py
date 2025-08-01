from celery import Celery
from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharecode.settings')

app = Celery('sharecode')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()