import os

from django.core.asgi import get_asgi_application
from .settings.base import DEBUG
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
import chat.routings

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings.production')        

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
            chat.routings.websocket_urlpatterns
        )
    )
    )
})