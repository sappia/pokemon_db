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


# class PokemonUpdateTestCase(APITestCase):
#     """test case to test updating of a pokemon entry"""
#     def test_update_pokemon(self):
#         pokemon = Pokemon.objects.get(id=895)
#         response = self.client.patch(
#             '/api/v1/pokemons/{}/'.format(pokemon.number),
#             {
#                 'name': 'strukuna',
#             },
#             format='json',
#         )
#         updated = Pokemon.objects.get(number=pokemon.number)
#         self.assertEqual(updated.name, 'strukuna')
#
#
# class PokemonDestroyTestCase(APITestCase):
#     """test case to test deletion of a pokemon entry"""
#     def test_delete_pokemon(self):
#         initial_pokemon_count = Pokemon.objects.count()
#         pokemon_number = Pokemon.objects.get(number=998)
#         self.client.delete('/api/v1/pokemons/{}/'.format(pokemon_number))
#         self.assertEqual(
#             Pokemon.objects.count(),
#             initial_pokemon_count - 1,
#         )
#         self.assertRaises(
#             Pokemon.DoesNotExist,
#             Pokemon.obects.get,
#             number=pokemon_number
#         )
