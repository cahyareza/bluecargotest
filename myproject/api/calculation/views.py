import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import FreightCalculationSerializer
from myproject.apps.countries.models import Country, Category
from django.shortcuts import get_object_or_404
from django.conf import settings


class FreightCalculationView(APIView):
    def post(self, request):
        serializer = FreightCalculationSerializer(data=request.data)
        if serializer.is_valid():
            country_id = serializer.validated_data['country_id']
            category_title = serializer.validated_data['category_title']
            origin_domestic_id = "444" # surabaya
            destination_id = serializer.validated_data['destination_id']
            weight = serializer.validated_data['weight']


            # Fetch necessary data from models
            country = Country.objects.get(id=country_id)
            category = get_object_or_404(Category, category_title=category_title, country_id=country.id)

            # Perform calculations international_price
            international_price = weight * category.price_per_kilo

            # get destination name
            url = f'https://api.rajaongkir.com/starter/city/?id={int(destination_id)}'

            headers = {
                'key': settings.RAJAONGKIR_API,
                'content-type': "application/x-www-form-urlencoded"
            }

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                results = data['rajaongkir']['results']
                destination = results["city_name"]
            else:
                destination = "Cannot get data city from raja ongkir"

            # get domestic cost from raja ongkir
            url = f"https://api.rajaongkir.com/starter/cost/?origin={origin_domestic_id}&destination={destination_id}&weight={weight}&courier=jne"
            headers = {
                'key': settings.RAJAONGKIR_API,
                'content-type': "application/x-www-form-urlencoded"
            }
            response = requests.post(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                domestic_price = data['rajaongkir']['results']['costs']['cost']['value']
                total_price = international_price + domestic_price
            else:
                domestic_price = "Cannot get data domestic cost from raja ongkir"
                total_price = "Cannot get data domestic cost from raja ongkir"

            # Prepare response data
            response_data = {
                'origin': country.country_name,
                'destination': destination,
                'category_name': category.category_title,
                'international_price': international_price,
                'domestic_price': domestic_price,
                'total_price': total_price
            }

            return Response(response_data)
        else:
            return Response(serializer.errors, status=400)
