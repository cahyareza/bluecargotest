from django.contrib import admin
from .models import Country


@admin.register(Country)
class CountryItemAdmin(admin.ModelAdmin):
    pass
