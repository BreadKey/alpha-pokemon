from django.shortcuts import render
from django.views import generic
from .models import Pokemon

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'pokedex/index.html'
    context_object_name = 'pokemon_spec_list'

    def get_queryset(self):
        return Pokemon.objects.order_by('-index_number')