from django.urls import path
from .views import profile, get_image

urlpatterns = [
    path("profile/", profile),
    path('image/<str:image>/', get_image, name='get_image'),

]