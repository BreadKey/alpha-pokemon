from django.db import models
from pokedex.models import *
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class SamplePokemon(models.Model):
    spec = models.ForeignKey(PokemonSpec, on_delete=models.CASCADE)

    level = models.IntegerField(default=50, validators=(MinValueValidator(1), MaxValueValidator(100)))

    nature = models.ForeignKey(PokemonNature, default=PokemonNature.objects.first(), on_delete=models.CASCADE)

    hp_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    attack_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    defense_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    sp_attack_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    sp_defense_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    speed_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))

    hp_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    attack_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    defense_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    sp_attack_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    sp_defense_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    speed_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))

    def base_stats(self):
        return {
            'hp': self.spec.base_hp,
            'attack': self.spec.base_attack,
            'defense': self.spec.base_defense,
            'special_attack': self.spec.base_special_attack,
            'special_defense': self.spec.base_special_defense,
            'speed': self.spec.base_speed
        }

    def EVs(self):
        return{
            'hp': self.hp_EV,
            'attack': self.attack_EV,
            'defense': self.defense_EV,
            'special_attack': self.sp_attack_EV,
            'special_defense': self.sp_defense_EV,
            'speed': self.sp_attack_EV
        }

    def IVs(self):
        return{
            'hp': self.hp_IV,
            'attack': self.attack_IV,
            'defense': self.defense_IV,
            'special_attack': self.sp_attack_IV,
            'special_defense': self.sp_defense_IV,
            'speed': self.speed_IV
        }