from django.contrib import admin
from .models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    """lists the fields that can be managed via the admin page"""
    list_display = ['number', 'name', 'height', 'weight', 'types', 'abilities']