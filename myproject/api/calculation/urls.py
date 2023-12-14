from django.urls import path
from .views import FreightCalculationView

app_name = "calculate"
urlpatterns = [
    path('', FreightCalculationView.as_view(), name='calculate'),
    # Other URL patterns...
]
