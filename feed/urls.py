from django.urls import path
from .views import feed, countries_search
urlpatterns = [
    path("feed/", feed, name="feed"),
    path("search/country/<str:country>", countries_search, name="search_country")
]
