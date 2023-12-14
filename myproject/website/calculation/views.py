import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from myproject.apps.countries.models import Category, Country
from myproject.website.categories.forms import CategoryForm


@login_required
def calculation(request):
    list_categories = Category.objects.all()
    list_counties = Country.objects.all()
    countriesstring = ''
    categoriesstring = ''

    for country in list_counties:
        b = "{'country_id':'%s', 'country_name': '%s', 'country_flag': '%s', 'country_currency': '%s'}," % (country.id, country.country_name,country.country_flag, country.country_currency)

        countriesstring = countriesstring + b

    for category in list_categories:
        b = "{'category_id':'%s', 'country_id': '%s', 'category_title': '%s', 'price_per_kilo': '%s'}," % (category.id, category.country_id,category.category_title, category.price_per_kilo)

        categoriesstring = categoriesstring + b

    # destination
    # Call Raja Ongkir API to search for cities
    url = f'https://api.rajaongkir.com/starter/city'

    headers = {
        'key': settings.RAJAONGKIR_API,
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.get(url, headers=headers)
    print(categoriesstring)
    if response.status_code == 200:
        data = response.json()
        results = data['rajaongkir']['results']
    else:
        results = []

    context = {
        'destinations': results,
        "countriesstring": countriesstring,
        "categoriesstring": categoriesstring,
    }
    return render(request, 'website/calculation/index.html', context)
