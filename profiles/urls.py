from django.urls import path
from .views import profile, get_image_trip, get_image_user, get_image_portate, trip, edit_profile

urlpatterns = [
    path("profile/<str:user>", profile, name="profile"),
    path('image/<str:title>/<str:image>/<str:user>/', get_image_trip, name='get_image_trip'),
    path('image/user/profile/<str:image>/<str:user>/', get_image_user, name='get_image_user'),
    path('image/user/portate/<str:image>/<str:user>/', get_image_portate, name='get_image_portate'),
    path('trip/<int:id>/', trip, name="trip"),
    path('edit_profile/', edit_profile, name="edit_profile")
]