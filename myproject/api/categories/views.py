from rest_framework import generics, filters

from myproject.apps.countries.models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    name = 'category-list'
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_title', 'price_per_kilo']

    def get_queryset(self):
        queryset = Category.objects.all()

        # Filtering by country_id if provided in query parameters
        country_id = self.request.query_params.get('country_id')
        if country_id:
            queryset = queryset.filter(country_id=country_id)

        return queryset
