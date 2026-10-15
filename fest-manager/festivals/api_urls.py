
from django.urls import path

from .views import api_views

app_name = 'festivals_api'


urlpatterns = [
    path("", api_views.FestivalListCreateView.as_view(), name="list"),
    path("<int:pk>/", api_views.FestivalRetrieveUpdateDestroyView.as_view(), name="detail"),
]
