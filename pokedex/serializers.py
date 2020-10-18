from rest_framework import serializers
from pokedex.admin import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """Add meta fields for the Pokemon model and validation for name, height and weight fields"""
    name = serializers.CharField(min_length=2, max_length=100)
    height = serializers.DecimalField(min_value=1.00, max_digits=None, decimal_places=2)
    weight = serializers.DecimalField(min_value=1.00, max_digits=None, decimal_places=2)

    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'types', 'abilities')
