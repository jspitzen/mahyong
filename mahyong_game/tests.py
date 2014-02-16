from django.test import TestCase

from mahyong_game.models import Player, Family

# Create your tests here.
class PlayerMethodTests(TestCase):

    def test_fullname_method(self):
        p = Player(first_name = 'Jorick', last_name = 'Spitzen')
        self.assertEqual(p.fullname(), 'Jorick Spitzen')

    def test_create_method_with_new_family(self):
        p = Player.create(first_name = 'Jorick', last_name = 'Spitzen')
        self.assertEqual(p.first_name, 'Jorick')
        self.assertEqual(p.last_name, 'Spitzen')
        self.assertEqual(Family.objects.count(), 1)

    def test_create_method_with_existing_family(self):
        fam = Family(name = 'Spitzen')
        p = Player.create(first_name = 'Jorick', last_name = 'Spitzen')
        self.assertEqual(p.family, fam)
        self.assertEqual(Family.objects.count(), 1)
