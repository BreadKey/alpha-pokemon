from django.test import TestCase
from pokedex.models import *
from .templatetags import calculator
from sample_maker.models import SamplePokemon

# Create your tests here.
class CalculatorTest(TestCase):

    def setUp(self):
        self.pokemon = make_pikachu()

    def test_calculate_stab1(self):
        move_type = PokemonType.objects.get(name__korean="전기")
        stab = calculator.calculate_STAB(self.pokemon.spec, move_type)
        expected_stab = 1.5

        self.assertEqual(stab, expected_stab)

    def test_calculate_stab2(self):
        move_type = PokemonType.objects.create(name=Name.objects.create(korean="불꽃"))
        stab = calculator.calculate_STAB(self.pokemon.spec, move_type)
        expected_stab = 1

        self.assertEqual(stab, expected_stab)

def make_pikachu():
    type = PokemonType.objects.get(name=Name.objects.get(korean="전기"))
    name = Name.objects.create(korean="피카츄")
    pikachu = PokemonSpec.objects.create(name=name, index_number=25)
    pikachu.types.add(type)

    return SamplePokemon.objects.create(spec=pikachu)

def make_types():
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="노말"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="불꽃"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="물"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="전기"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="풀"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="얼음"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="격투"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="독"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="땅"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="비행"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="에스퍼"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="벌레"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="바위"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="고스트"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="드래곤"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="악"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="강철"))
    PokemonType.objects.get_or_create(name=Name.objects.create(korean="페어리"))


