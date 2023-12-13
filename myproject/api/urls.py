from django.urls import path, include
from .views import ApiRoot

app_name = "api"
urlpatterns = [
    path('countries/', include('myproject.api.countries.urls')),
    path('categories/', include('myproject.api.categories.urls')),
    path('destination/', include('myproject.api.destination.urls')),
    path('list/', ApiRoot.as_view(), name=ApiRoot.name),
]
