from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'pokedex/home.html'

class PokemonIndexView(generic.ListView):
    template_name = 'pokedex/pokemon_index.html'
    context_object_name = 'pokemon_spec_list'

    def get_queryset(self):
        return PokemonSpec.objects.order_by('index_number')

class PokemonDetailView(generic.DetailView):
    model = PokemonSpec
    template_name = 'pokedex/pokemon_detail.html'

class MoveIndexView(generic.ListView):
    template_name = 'pokedex/move_index.html'
    context_object_name = 'move_list'

    def get_queryset(self):
        return PokemonMove.objects.order_by('id')

class MoveDetailView(generic.DetailView):
    model = PokemonMove
    template_name = 'pokedex/move_detail.html'

class AbilityIndexView(generic.ListView):
    template_name = 'pokedex/ability_index.html'
    context_object_name = 'ability_list'

    def get_queryset(self):
        return PokemonAbility.objects.order_by('id')

class AbilityDetailView(generic.DetailView):
    model = PokemonAbility
    template_name = 'pokedex/ability_detail.html'