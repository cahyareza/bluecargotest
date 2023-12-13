from rest_framework import serializers

from myproject.apps.countries.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("country_id", "category_title", "price_per_kilo")
