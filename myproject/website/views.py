from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from myproject.apps.countries.models import Country, Category


def index(request):
    return render(request, 'website/index.html')

@login_required
def dashboard(request):
    list_countries = Country.objects.all()[0:2]
    list_categories = Category.objects.all()[0:2]
    context = {
        'countries': list_countries,
        'categories': list_categories,
    }
    return render(request, 'website/dashboard.html', context)
