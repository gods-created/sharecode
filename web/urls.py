from django.urls import path
from .views import start_page, ide_page

app_name = 'web'

urlpatterns = [
    path('start/', start_page, name='start_page'),
    path('ide/', ide_page, name='ide_page'),
]