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
    special_attack_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    special_defense_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))
    speed_EV = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(252)))

    hp_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    attack_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    defense_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    special_attack_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
    special_defense_IV = models.IntegerField(default=31, validators=(MinValueValidator(0), MaxValueValidator(31)))
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
            'special_attack': self.special_attack_EV,
            'special_defense': self.special_defense_EV,
            'speed': self.special_attack_EV
        }

    def IVs(self):
        return{
            'hp': self.hp_IV,
            'attack': self.attack_IV,
            'defense': self.defense_IV,
            'special_attack': self.special_attack_IV,
            'special_defense': self.special_defense_IV,
            'speed': self.speed_IV
        }

    def hidden_power_type(self):
        IVs = self.IVs()
        type_value = (IVs['hp'] % 2) + \
                     (2 * (IVs['attack'] % 2)) + (4 * (IVs['defense'] % 2)) + \
                     (8 * (IVs['speed'] % 2)) + \
                     (16 * (IVs['special_attack'] % 2)) + (32 * (IVs['special_defense'] % 2));

        type_value *= 15
        type_value /= 63
        type_value = int(type_value)

        if type_value == 0:
            type = PokemonType.objects.get(name__korean='격투')
        elif type_value == 1:
            type = PokemonType.objects.get(name__korean='비행')
        elif type_value == 2:
            type = PokemonType.objects.get(name__korean='독')
        elif type_value == 3:
            type = PokemonType.objects.get(name__korean='땅')
        elif type_value == 4:
            type = PokemonType.objects.get(name__korean='바위')
        elif type_value == 5:
            type = PokemonType.objects.get(name__korean='벌레')
        elif type_value == 6:
            type = PokemonType.objects.get(name__korean='고스트')
        elif type_value == 7:
            type = PokemonType.objects.get(name__korean='강철')
        elif type_value == 8:
            type = PokemonType.objects.get(name__korean='불꽃')
        elif type_value == 9:
            type = PokemonType.objects.get(name__korean='물')
        elif type_value == 10:
            type = PokemonType.objects.get(name__korean='풀')
        elif type_value == 11:
            type = PokemonType.objects.get(name__korean='전기')
        elif type_value == 12:
            type = PokemonType.objects.get(name__korean='에스퍼')
        elif type_value == 13:
            type = PokemonType.objects.get(name__korean='얼음')
        elif type_value == 14:
            type = PokemonType.objects.get(name__korean='드래곤')
        elif type_value == 15:
            type = PokemonType.objects.get(name__korean='악')

        return type