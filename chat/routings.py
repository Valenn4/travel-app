from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path(r'ws/<str:uuid>/', consumers.ChatConsumer.as_asgi())
]