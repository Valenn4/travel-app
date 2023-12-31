from django.urls import path, include
from api_rest import views

urlpatterns = [
    path("api/v1/users/<str:contains>", views.UserContainsViewSet.as_view(), name="users"),
    path("api/v1/following/<str:username>", views.FollowingViewSet.as_view(), name="followings"),
    path("api/v1/user/<str:username>", views.UserViewSet.as_view(), name="user"),
    path("api/v1/publication/<int:id>", views.PublicationViewSet.as_view(), name="publication")
]
