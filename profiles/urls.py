from django.urls import path
from .views import profile, get_image_trip, get_image_user, get_image_portate, new_trip, new_message, trip, edit_profile

urlpatterns = [
    path("profile/", profile),
    path('image/<str:location>/<str:image>/', get_image_trip, name='get_image_trip'),
    path('image/user/profile/<str:image>/', get_image_user, name='get_image_user'),
    path('image/user/portate/<str:image>/', get_image_portate, name='get_image_portate'),
    path('new_trip/', new_trip),
    path('new_message/', new_message),
    path('trip/<int:id>/', trip),
    path('edit_profile/<int:id>', edit_profile)
]