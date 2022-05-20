from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_location', 'capital']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_location', 'capital']


@admin.register(State)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_location', 'capital']


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'state', 'city']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']