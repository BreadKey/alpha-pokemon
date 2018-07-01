from django.test import TestCase
from .models import Name, PokemonType, Pokemon

# Create your tests here.
class PokemonTest(TestCase):
    def test_create(self):
        name = Name.objects.create(korean='피카츄', english='pikachu')
        pikachu = Pokemon.objects.create(name=name)
        self.assertEqual(pikachu.name.korean, '피카츄')