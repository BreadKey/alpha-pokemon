from django.shortcuts import render
from pokedex.models import *
from django.views import generic
from .models import SamplePokemon
from .forms import SamplePokemonForm

# Create your views here.

class SelectPokemonView(generic.ListView):
    template_name = 'sample_maker/select_pokemon.html'
    context_object_name = 'pokemon_list'

    def get_queryset(self):
        return PokemonSpec.objects.order_by('index_number')

class SMT(generic.TemplateView):
    template_name = 'sample_maker/smt.html'

    def get(self, request, *args, **kwargs):
        self.sample_pokemon = SamplePokemon(spec=PokemonSpec.objects.get(pk=kwargs['pk']))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SMT, self).get_context_data(**kwargs)
        context['sample_pokemon'] = self.sample_pokemon
        context['form'] = SamplePokemonForm()
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

class SampleMakerView(generic.TemplateView):
    template_name = 'sample_maker/sample_maker.html'

    def get(self, request, *args, **kwargs):
        self.sample_pokemon = SamplePokemon(spec=PokemonSpec.objects.get(pk=kwargs['pk']))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SampleMakerView, self).get_context_data(**kwargs)
        context['sample_pokemon'] = self.sample_pokemon
        context['form'] = SamplePokemonForm()
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