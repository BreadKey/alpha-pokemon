from .models import SamplePokemon
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class SamplePokemonForm(forms.ModelForm):
    class Meta:
        model = SamplePokemon
        fields = (
            'hp_EV', 'attack_EV', 'defense_EV', 'special_attack_EV', 'special_defense_EV', 'speed_EV',
            'hp_IV', 'attack_IV', 'defense_IV', 'special_attack_IV', 'special_defense_IV', 'speed_IV',
        )
        widgets = {}
        for key in fields:
            if key.split('_').pop() == 'EV':
                widgets[key] = forms.NumberInput(attrs={'max': 252, 'min': 0, 'id': key, 'oninput': "EV_changed('" + key + "')"})
            elif key.split('_').pop() == 'IV':
                widgets[key] = forms.NumberInput(attrs={'max': 31, 'min': 0, 'id': key, 'oninput': "IV_changed('" + key + "')"})