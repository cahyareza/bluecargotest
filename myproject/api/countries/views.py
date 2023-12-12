from rest_framework import generics, filters

from myproject.apps.countries.models import Country
from .serializers import CountrySerializer

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    name = 'country-list'
    filter_backends = [filters.SearchFilter]
    search_fields = ['country_name', 'country_flag', 'country_currency']
