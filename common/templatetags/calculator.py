from pokedex.models import *
from django import template
from sample_maker.models import SamplePokemon

register = template.Library()

@register.simple_tag
def calculate_STAB(pokemon_spec: PokemonSpec, move_type: PokemonType):
    for pokemon_type in pokemon_spec.types.all():
        if pokemon_type.pk == move_type.pk:
            return 1.5
    return 1
