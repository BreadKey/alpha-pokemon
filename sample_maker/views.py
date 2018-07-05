from django.shortcuts import render
from pokedex.models import *
from django.views import generic

# Create your views here.

class SelectPokemonView(generic.ListView):
    template_name = 'sample_maker/select_pokemon.html'
    context_object_name = 'pokemon_list'

    def get_queryset(self):
        return PokemonSpec.objects.order_by('-index_number')

class SampleMakerView(generic.DetailView):
    model = PokemonSpec
    template_name = 'sample_maker/sample_maker.html'