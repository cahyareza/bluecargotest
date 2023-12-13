from django.urls import path
from .views import CategoryList

app_name = "categories"
urlpatterns = [
    path('', CategoryList.as_view(), name=CategoryList.name),
]
