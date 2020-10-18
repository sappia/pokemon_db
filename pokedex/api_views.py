from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from pokedex.serializers import PokemonSerializer
from pokedex.models import Pokemon


class PokemonPagination(LimitOffsetPagination):
    """defines default limits for pagination of pokemon list"""
    default_limit = 10
    max_limit = 100


class PokemonList(ListAPIView):
    """API for listing pokemons and providing filter, search and pagination functionalities"""
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('number',)
    search_fields = ('name', 'types')
    pagination_class = PokemonPagination

    def get_queryset(self):
        types = self.request.query_params.get('types', None)
        if types is None:
            return super().get_queryset()
        queryset = Pokemon.objects.all()
        if 'poison' in types:
            return queryset.filter(
                types__icontains='poison'
            )
        return queryset


class PokemonCreate(CreateAPIView):
    """API for creating a new Pokemon"""
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        try:
            height = request.data.get('height')
            weight = request.data.get('weight')
            if height is not None and float(height) <= 0.0:
                raise ValidationError({'height': 'Must be above 0.0'})
            if weight is not None and float(weight) <= 0.0:
                raise ValidationError({'weight': 'Must be above 0.0'})
        except ValueError:
            raise ValidationError({'height/weight': 'A valid number is required.'})
        return super().create(request, *args, **kwargs)


class PokemonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """API for retrieving, updating and deleting a Pokemon"""
    queryset = Pokemon.objects.all()
    lookup_field = 'number'
    serializer_class = PokemonSerializer

    def delete(self, request, *args, **kwargs):
        pokemon_number = request.data.get('number')
        response = super().delete(request, *args, **kwargs)
        # if successfully deleted, also delete from the cache
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('pokemon_data_{}'.format(pokemon_number))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        # if successfully updated, also update the cache
        if response.status_code == 200:
            from django.core.cache import cache
            pokemon = response.data
            cache.set('pokemon_data_{}'.format(pokemon['number']), {
                'name': pokemon['name'],
                'types': pokemon['types'],
                'abilities': pokemon['abilities']
            })
        return response
