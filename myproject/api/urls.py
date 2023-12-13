from django.urls import path, include

app_name = "api"
urlpatterns = [
    path('countries/', include('myproject.api.countries.urls')),
    path('categories/', include('myproject.api.categories.urls')),
    path('destination/', include('myproject.api.destination.urls')),
]
