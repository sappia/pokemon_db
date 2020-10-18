"""Loads data in pokedex_data.csv file into the Pokemon table in sqlite database#."""
from csv import DictReader
from django.core.management import BaseCommand
from pokedex.models import Pokemon

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pokemon data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pokedex_data.csv into our Pokemon model"

    def handle(self, *args, **options):
        if Pokemon.objects.exists():
            print('Pokemon data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading pokedex data for available pokemon")
        for row in DictReader(open('./pokedex_data.csv')):
            poke = Pokemon()
            poke.number = row['number']
            poke.name = row['name']
            poke.height = row['height']
            poke.weight = row['weight']
            poke.types = row['types']
            poke.abilities = row['abilities']
            poke.save()
