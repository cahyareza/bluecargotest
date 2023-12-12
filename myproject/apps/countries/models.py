from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=30)
    country_flag = models.CharField(max_length=100)
    country_currency = models.CharField(max_length=5)


class Category(models.Model):
    country_id = models.CharField(max_length=5)
    category_title = models.CharField(max_length=30)
    price_per_kilo = models.IntegerField()
