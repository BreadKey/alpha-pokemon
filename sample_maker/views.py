from django.shortcuts import render
from pokedex.models import *
from django.views import generic

# Create your views here.

class SelectPokemonView(generic.ListView):
    template_name = 'sample_maker/select_pokemon.html'
    context_object_name = 'pokemon_list'

    def get_queryset(self):
        return PokemonSpec.objects.order_by('index_number')

class SampleMakerView(generic.TemplateView):
    template_name = 'sample_maker/sample_maker.html'

    def get_context_data(self, **kwargs):
        context = super(SampleMakerView, self).get_context_data(**kwargs)
        context['pokemonspec'] = PokemonSpec.objects.get(pk=kwargs['pk'])
        context['natures'] = PokemonNature.objects.order_by('id')
        context['stats'] = [
            Name.objects.get(korean='HP'),
            Name.objects.get(korean='공격'),
            Name.objects.get(korean='방어'),
            Name.objects.get(korean='특수공격'),
            Name.objects.get(korean='특수방어'),
            Name.objects.get(korean='스피드')
        ]
        context['formal_stats'] = [
            'hp',
            'attack',
            'defense',
            'special_attack',
            'special_defense',
            'speed'
        ]
        context['number_of_moves'] = range(4)
        context['pokemontypes'] = PokemonType.objects.all()

        return context