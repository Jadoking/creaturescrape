from django.db import models
from .enums import CreatureTypes, PokemonTypes, DigimonLevels


class Creature(models.Model):
    name = models.CharField(max_length=100)
    creature_type = models.CharField(
            max_length=100,
            choices=CreatureTypes.choices)
    img_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'creature_type',)


class Pokemon(models.Model):
    type1 = models.CharField(
            max_length=10,
            choices=PokemonTypes.choices)
    type2 = models.CharField(
            max_length=10,
            choices=PokemonTypes.choices)
    creature = models.OneToOneField(Creature, on_delete=models.CASCADE)


class Digimon(models.Model):
    level = models.CharField(
            max_length=12,
            choices=DigimonLevels.choices)
    creature = models.OneToOneField(Creature, on_delete=models.CASCADE)
