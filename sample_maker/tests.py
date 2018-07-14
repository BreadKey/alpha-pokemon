from django.test import TestCase
from .templatetags import manage_sample
from .models import SamplePokemon
from pokedex.models import *
from common import constants
from common.tests import make_pikachu, make_types

# Create your tests here.

class TestManageSample(TestCase):
    def setUp(self):
        make_types()
        self.sample = make_pikachu()

    def test_set_EV_bigger_than_max(self):
        manage_sample.set_effort_value(self.sample, 'hp', 255)
        hp_EV = self.sample.hp_EV
        expected_hp_EV = constants.MAX_EV

        self.assertEqual(hp_EV, expected_hp_EV)

    def test_set_EV_smaller_than_min(self):
        manage_sample.set_effort_value(self.sample, 'hp', -10)
        hp_EV = self.sample.hp_EV
        expected_hp_EV = constants.MIN_EV

        self.assertEqual(hp_EV, expected_hp_EV)

    def test_set_EV_not_integer(self):
        manage_sample.set_effort_value(self.sample, 'hp', 'asd')
        hp_EV = self.sample.hp_EV
        expected_hp_EV = 0

        self.assertEqual(hp_EV, expected_hp_EV)

    def test_set_EV_over_max_sum(self):
        manage_sample.set_effort_value(self.sample, 'hp', 252)
        manage_sample.set_effort_value(self.sample, 'attack', 252)
        manage_sample.set_effort_value(self.sample, 'defense', 252)

        defense_EV = self.sample.defense_EV
        expected_defense_EV = 6

        self.assertEqual(defense_EV, expected_defense_EV)

    def test_hidden_power1(self):
        hidden_power_type = self.sample.hidden_power_type()
        expected_HPT = PokemonType.objects.get(name__korean="악")

        self.assertEqual(hidden_power_type, expected_HPT)