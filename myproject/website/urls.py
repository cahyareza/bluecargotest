from django.urls import path, include
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include(('myproject.website.accounts.urls', "accounts"), namespace='accounts')),
    path('countries/', include(('myproject.website.countries.urls', "countries"), namespace="countries")),
]
