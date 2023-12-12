from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from myproject.apps.countries.models import Country


def index(request):
    return render(request, 'website/index.html')
