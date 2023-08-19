from django.urls import path
from .views import chat, new_message
urlpatterns = [
    path('chat/<str:uuid>', chat),
    path('new_message/<str:room>', new_message)
]
