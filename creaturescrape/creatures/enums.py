from django.utils.translation import gettext_lazy as _
from django.db import models


class CreatureTypes(models.TextChoices):
    POKEMON = "POKEMON", _('Pokemon')
    DIGIMON = "DIGIMON", _('Digimon')


class PokemonTypes(models.TextChoices):
    NORMAL = "NORMAL", _('Normal')
    FIRE = "FIRE", _('Fire')
    WATER = "WATER", _('Water')
    GRASS = "GRASS", _('Grass')
    ELECTRIC = "ELECTRIC", _('Electric')
    ICE = "ICE", _('Ice')
    FIGHTING = "FIGHTING", _('Fighting')
    POISON = "POISON", _('Poison')
    GROUND = "GROUND", _('Ground')
    FLYING = "FLYING", _('Flying')
    PSYCHIC = "PSYCHIC", _('Psychic')
    BUG = "BUG", _('Bug')
    ROCK = "ROCK", _('Rock')
    GHOST = "GHOST", _('Ghost')
    DARK = "DARK", _('Dark')
    DRAGON = "DRAGON", _('Dragon')
    STEEL = "STEEL", _('Steel')
    FAIRY = "FAIRY", _('Fairy')
    NONE = "NONE", _('None')

class DigimonLevels(models.TextChoices):
    FRESH = "FRESH", _('Fresh')
    IN_TRAINING = "IN TRAINING", _('In Training')
    ROOKIE = "ROOKIE", _('Rookie')
    CHAMPION = "CHAMPION", _('Champion')
    ULTIMATE = "ULTIMATE", _('Ultimate')
    ARMOR = "ARMOR", _('Armor')
    MEGA = "MEGA", _('Mega')
