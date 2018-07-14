from .models import SamplePokemon
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class SamplePokemonForm(forms.ModelForm):
    class Meta:
        model = SamplePokemon
        fields = ('hp_EV', 'attack_EV', 'defense_EV', 'special_attack_EV', 'special_defense_EV', 'speed_EV')
        widgets = {}
        for key in fields:
            if key.split('_').pop() == 'EV':
                widgets[key] = forms.NumberInput(attrs={'max': 252, 'min': 0, 'id': key, 'oninput': "EV_changed('" + key + "')"})
