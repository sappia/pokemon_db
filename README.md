# pokemon_db

## Overview
A pokemon directory built using Django and Django Rest framework. The data for pokemons is gathered from the [Pokebase library](https://github.com/PokeAPI/pokebase). The home page shows a list of all pokemons found so far. This app provides API to view, add, delete and update a pokemon. It also provides features like pagination, filtering a pokemon by pokemon number/ID or search by a word (eg: pokemon name, type or ability).

## Contents
This project consists of the files used to create and load data, django files to build the web application and api and template html files to show the data in the sqllite db on the web application. 

## Installation
This project was built using Python 3.8.5 and Django 3.1.2 versions. Versions of all the libraries used can be seen in requirements.txt file.

## Usage
1. To load data into the sqlite database, run the below command from the main pokemon_db directory:
```
python manage.py load_pokedex_data
```
2. To run the django server, run the below command from the main pokemon_db directory:
```
python manage.py runserver
```
3. The application can then be accessed on a browser at http://localhost:8000/ which lists all the pokemons. Each one can be clicked on the see its details.

4. To access the api listing all the pokemon using rest framework, go to http://localhost:8000/api/v1/pokemons/. Clicking the Filters button will allow filtering by Pokemon number/ID or search by a pokemon name, type or ability.

5. A pokemon details can be accessed via the api using http://localhost:8000/api/v1/pokemons/<int: pokemon_number>/ (eg: http://localhost:8000/api/v1/pokemons/1/) which allows to view, update or delete a pokemon.

6. A new pokemon can be added using http://localhost:8000/api/v1/pokemons/new/ and filling in all the fields for a new pokemon.

