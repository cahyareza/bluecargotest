from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'categories': reverse('api:categories:category-list', request=request),
            'countries': reverse('api:countries:country-list', request=request),
            'destination': reverse('api:destination:destination-list', request=request),
            })
