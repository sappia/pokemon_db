from django.db import models


class Pokemon(models.Model):
    """model used to store details of all Pokemons"""
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    types = models.CharField(max_length=200)
    abilities = models.CharField(max_length=200)
