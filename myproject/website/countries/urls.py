from django.urls import path

from . import views

urlpatterns = [
    path('', views.countries, name='index'),
    path('add', views.add_country, name='add_country'),
    path('edit/<int:id>', views.edit_country, name='edit_country'),
    path('delete/<int:id>', views.delete_country, name='delete_country'),
]
