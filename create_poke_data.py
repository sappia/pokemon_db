"""This file creates a csv file (pokedex_data.csv) with few details for all pokemon available in pokebase library."""
import csv
import pokebase as pb

# write pokedex entries to a csv file
column_headers = ['number', 'name', 'height', 'weight', 'types', 'abilities']
with open("pokedex_data.csv", "w") as c:
    w = csv.writer(c)
    w.writerow(column_headers)

with open("pokedex_data.csv", "a") as c:
    for i in range(1, 894):
        pokemon = pb.pokemon(i)
        number = pokemon.id
        name = pokemon.name
        height = pokemon.height
        weight = pokemon.weight

        types = pokemon.types
        num_of_type = len(types)
        type = ''
        for i in range(0, num_of_type):
            type = type + pokemon.types[i].type.name + '|'
        type = type.rstrip('|')

        abilities = pokemon.abilities
        num_of_abilities = len(abilities)
        ability = ''
        for i in range(0, num_of_abilities):
            ability = ability + pokemon.abilities[i].ability.name + '|'
        ability = ability.rstrip('|')

        c.write(str(number) + "," + name + "," + str(height) + "," + str(weight) + "," + type + "," + ability + "\n")
