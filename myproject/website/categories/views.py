from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from myproject.apps.countries.models import Category
from myproject.website.categories.forms import CategoryForm


@login_required
def categories(request):
    list_countries = Category.objects.all()
    context = {
        'categories': list_countries
    }
    return render(request, 'website/categories/index.html', context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            # object = form.save(commit=False)
            form.save()
        return redirect("website:categories:index")
    else:
        form = CategoryForm(request.POST or None)

    return render(request, "website/categories/add_category.html", {'form': form})


def edit_category(request, id):
    category_instance = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, instance=category_instance)
        if form.is_valid():
            form.save()
        return redirect("website:categories:index")
    else:
        form = CategoryForm(request.POST or None, instance=category_instance)

    return render(request, "website/categories/add_category.html", {'form': form})


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("website:categories:index")
