# Generated by Django 3.2.23 on 2023-12-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(max_length=5)),
                ('category_title', models.CharField(max_length=30)),
                ('price_per_kilo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
                ('country_flag', models.CharField(max_length=100)),
                ('country_currency', models.CharField(max_length=5)),
            ],
        ),
    ]
