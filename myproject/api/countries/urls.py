from django.urls import path
from .views import CountryList

app_name = "countries"
urlpatterns = [
    path('', CountryList.as_view(), name=CountryList.name),
]
