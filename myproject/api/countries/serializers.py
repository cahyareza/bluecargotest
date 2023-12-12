from rest_framework import serializers

from myproject.apps.countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("country_name", "country_flag", "country_currency")
