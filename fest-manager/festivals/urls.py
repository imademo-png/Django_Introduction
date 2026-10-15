from django.urls import path

from . import views
from .views import festival_list

app_name = 'festivals'


urlpatterns = [
    path("", views.festival_list, name="list"),
    path("<int:fest_id>/", views.festival_detail, name="detail"),
]