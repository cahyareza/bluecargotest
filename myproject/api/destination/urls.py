from django.urls import path
from .views import DestinationSearchView

app_name = "destination"
urlpatterns = [
    path('', DestinationSearchView.as_view(), name='destination-list'),
]
