from pokedex.models import *
from ..models import SamplePokemon
from django import template
from common import constants

register = template.Library()

@register.simple_tag
def set_effort_value(sample: SamplePokemon, stat, value):
    print(stat, value)
    try:
        value = int(value)
    except:
        value = 0

    if value < constants.MIN_EV:
        value = constants.MIN_EV
    elif value > constants.MAX_EV:
        value = constants.MAX_EV

    sum = 0

    for EV_stat, EV_value in sample.EVs().items():
        if EV_stat == stat:
            pass
        else:
            sum += EV_value
    sum += value

    if sum > constants.MAX_SUM_OF_EVS:
        value -= (sum - constants.MAX_SUM_OF_EVS)

    if stat == 'hp':
        sample.hp_EV = value
    elif stat == 'attack':
        sample.attack_EV = value
    elif stat == 'defense':
        sample.defense_EV = value
    elif stat == 'special_attack':
        sample.special_attack_EV = value
    elif stat == 'special_defense':
        sample.special_defense_EV = value
    elif stat == 'speed':
        sample.speed_EV = value

    return value