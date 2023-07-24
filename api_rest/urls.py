from django.urls import path, include
from api_rest import views

urlpatterns = [
    path("api/v1/users/<str:contains>", views.UserViewSet.as_view(), name="users")
]
