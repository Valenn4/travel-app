from django.urls import path
from .views import profile, get_image_trip, get_image_user, get_image_portate, new_trip, new_message, trip, edit_profile

urlpatterns = [
    path("profile/<str:user>", profile, name="profile"),
    path('image/<str:location>/<str:image>/<str:user>/', get_image_trip, name='get_image_trip'),
    path('image/user/profile/<str:image>/<str:user>/', get_image_user, name='get_image_user'),
    path('image/user/portate/<str:image>/<str:user>/', get_image_portate, name='get_image_portate'),
    path('new_trip/', new_trip, name="new_trip"),
    path('new_message/', new_message, name="new_message"),
    path('trip/<int:id>/', trip, name="trip"),
    path('edit_profile/', edit_profile, name="edit_profile")
]