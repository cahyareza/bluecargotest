from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from myproject.apps.countries.models import Country
from myproject.website.countries.forms import CountryForm


@login_required
def countries(request):
    list_countries = Country.objects.all()
    context = {
        'countries': list_countries
    }
    return render(request, 'website/countries/index.html', context)


def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST or None)
        if form.is_valid():
            # object = form.save(commit=False)
            form.save()
        return redirect("website:countries:index")
    else:
        form = CountryForm(request.POST or None)

    return render(request, "website/countries/add_country.html", {'form': form})


def edit_country(request, id):
    list_countries = Country.objects.get(id=id)
    if request.method == 'POST':
        form = CountryForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("website:countries:index")
    else:
        form = CountryForm(request.POST or None, request.FILES)

    return render(request, "website/countries/add_country.html", {'form': form})


def delete_country(request, id):
    country = get_object_or_404(Country, id=id)
    country.delete()
    return redirect("website:countries:index")
