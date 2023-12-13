import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings


class DestinationSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('search')

        if not search_query:
            return Response({"message": "Please provide a valid search query"}, status=400)

        # Call Raja Ongkir API to search for cities
        url = f'https://api.rajaongkir.com/starter/city'

        headers = {
            'key': settings.RAJAONGKIR_API,
            'content-type': "application/x-www-form-urlencoded"
        }


        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data['rajaongkir']['results']
            filtered_results = [result for result in results if result['city_name'] == search_query]
            return Response(filtered_results)
        else:
            return Response({"message": "Failed to fetch data from Raja Ongkir API"}, status=500)
