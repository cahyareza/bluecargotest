from django import forms
from myproject.apps.countries.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['country_id', 'category_title', 'price_per_kilo']

