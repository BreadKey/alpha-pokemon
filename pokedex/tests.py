from django.test import TestCase
from .models import Name, PokemonType, PokemonSpec

# Create your tests here.
class PokemonTest(TestCase):
    def test_create(self):
        name = Name.objects.create(korean='피카츄', english='pikachu')
        pikachu = PokemonSpec.objects.create(name=name)
        self.assertEqual(pikachu.name.korean, '피카츄')

    def test_sum_of_base_stats(self):
        p:PokemonSpec = PokemonSpec.objects.create(name=Name.objects.create(korean='뮤'))
        self.assertEqual(600, p.sum_of_base_stats())