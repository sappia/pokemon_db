from django.shortcuts import render
from django.http import Http404
from .models import Pokemon


def home(request):
    """home view to render list of all Pokemons"""
    pokemons = Pokemon.objects.all()
    return render(request, 'home.html', {'pokemons': pokemons})


def pokemon_detail(request, pokemon_id):
    """pokemon_detail view to render details of a selected Pokemon"""
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        raise Http404('Pokemon not found')
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})