from django.urls import path
from .views import profile, get_image_trip, get_image_user, new_trip

urlpatterns = [
    path("profile/", profile),
    path('image/<str:location>/<str:image>/', get_image_trip, name='get_image_trip'),
    path('image/<str:image>/', get_image_user, name='get_image_user'),
    path('new_trip/', new_trip)

]