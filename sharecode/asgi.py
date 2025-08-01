import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from django.core.asgi import get_asgi_application
from .consumers import CodeShareConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharecode.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/code/(?P<room>\w+)/$', CodeShareConsumer.as_asgi())
        ])
    )
})
