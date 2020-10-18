from rest_framework import status
from rest_framework.test import APITestCase
from pokedex.models import Pokemon


class PokemonListTestCase(APITestCase):
    """test case to test get api for list of pokemons"""
    def test_list_pokemon(self):
        pokemon_count = Pokemon.objects.count()
        response = self.client.get('/api/v1/pokemons/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], pokemon_count)
        self.assertEqual(len(response.data['results']), pokemon_count)


class PokemonCreateTestCase(APITestCase):
    """test case to test creation of a pokemon entry"""
    def test_create_pokemon(self):
        initial_pokemon_count = Pokemon.objects.count()
        pokemon_attrs = {
            'number': 996,
            'name': 'nokuna',
            'height': 30,
            'weight': 75,
            'types': 'water',
            'abilities': 'freezes',
        }
        response = self.client.post('/api/v1/pokemons/new/', pokemon_attrs, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Pokemon.objects.count(),
            initial_pokemon_count + 1,
        )


