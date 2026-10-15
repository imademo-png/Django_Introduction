from django.urls import path

from . import views

app_name = 'festivals'


urlpatterns = [
    path("", views.FestivalListView.as_view(), name="list"),
    path("<int:fest_id>/", views.FestivalDetailView.as_view(), name="detail"),
]
