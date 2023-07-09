from django.urls import path
from .views import profile, get_image, new_trip

urlpatterns = [
    path("profile/", profile),
    path('image/<str:image>/', get_image, name='get_image'),
    path('new_trip/', new_trip)

]