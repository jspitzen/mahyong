from django.test import TestCase

from mahyong_game.models import Player, Family, Game, Round, PlayerRound

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

class PlayerRoundMethodTests(TestCase):
    
    def setUp(self):
        self.jorick = Player(first_name = 'Jorick', last_name = 'Spitzen')
        self.titus  = Player(first_name = 'Titus' , last_name = 'Spitzen')
        self.game   = Game()
        self._round  = Round(game = self.game)

    def test_calculateGameScore_no_east_no_mahyong(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'North', 
                                boardScore = 10)

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20)

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, -10)
        self.assertEqual(pr_titus.gameScore, 10)
    
    def test_calculateGameScore_east_no_mahyong(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'East', 
                                boardScore = 10)

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20)

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, -20)
        self.assertEqual(pr_titus.gameScore, 20)

    def test_calculateGameScore_no_east_mahyong_higher(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'North', 
                                boardScore = 10)

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20,
                                mahyong    = True)

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, -10)
        self.assertEqual(pr_titus.gameScore, 10)

    def test_calculategameScore_east_mahyong_higher(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'East', 
                                boardScore = 10)

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20,
                                mahyong    = True)

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, -20)
        self.assertEqual(pr_titus.gameScore, 20)

    def test_calculategameScore_no_east_mahyong_lower(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'North', 
                                boardScore = 10,
                                mahyong    = True,
                                )

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20,
                                )

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, 0)
        self.assertEqual(pr_titus.gameScore, 0)

    def test_calculategameScore_east_mahyong_lower(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'East', 
                                boardScore = 10,
                                mahyong    = True,
                                )

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 20,
                                )

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, 0)
        self.assertEqual(pr_titus.gameScore, 0)

    def test_calculategameScore_east_mahyong_self(self):
        pr_jorick = PlayerRound(player     = self.jorick, 
                                _round      = self._round, 
                                position   = 'East', 
                                boardScore = 20,
                                mahyong    = True,
                                )

        pr_titus  = PlayerRound(player     = self.titus, 
                                _round      = self._round, 
                                position   ='West', 
                                boardScore = 10,
                                )

        PlayerRound.calculateGameScore(playerround1 = pr_jorick, playerround2 = pr_titus)
        self.assertEqual(pr_jorick.gameScore, 20)
        self.assertEqual(pr_titus.gameScore, -20)

