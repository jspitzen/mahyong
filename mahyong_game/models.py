from django.db import models

from mahyong_game.utils import *

# Create your models here.
class Player(models.Model):
    first_name   = models.CharField(max_length = 32)
    last_name    = models.CharField(max_length = 32)
    email        = models.EmailField(blank = True)
    email_scores = models.BooleanField(default = False)
    family       = models.ForeignKey('Family', blank = True)

    @classmethod
    def create(cls, first_name, last_name, email=""):
        # Check if family with this name already exists, otherwise create it
        fam, created = Family.objects.get_or_create(name=last_name)
        
        # Call default constructor with new family
        newPerson = cls(first_name = first_name, 
                        last_name = last_name, 
                        email = email,
                        family = fam)
        return newPerson

    def fullname(self):
        # Return string representation of the full name of the player
        return str.format("{} {}", self.first_name, self.last_name)

    def link(self):
        # Return the link to the detailview for this Player
        return object_detail_link(self)

    def count_games(self):
        # Return the number of started games
        return self.games.count()

    def __unicode__(self):
        return self.fullname()

    class Meta:
        ordering = ["last_name", "first_name"]

class Family(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    
    def __unicode__(self):
        return self.name

    def __eq__(self, other):
        # Override equals method to check for name
        return isinstance(other, self.__class__) and self.name == other.name

    class Meta:
        verbose_name_plural = 'Families'

class Game(models.Model):
    name         = models.CharField(max_length = 64, blank = True)
    date_started = models.DateField()
    players      = models.ManyToManyField('Player', related_name='games')
    finished     = models.DateField(blank = True, null = True)

    def __unicode__(self):
        return str.format("{}: {}", self.id, self.name)

    def link(self):
        # Return the link to the detailview for this Game
        return object_detail_link(self)

class Round(models.Model):
    players = models.ManyToManyField('Player', through='PlayerRound')
    game    = models.ForeignKey('Game')
    
    def __unicode__(self):
        return str.format("Round {}", self.id)

class PlayerRound(models.Model):
    # Set up position enum
    POSITION_CHOICES = (
        ('N', 'North'),
        ('E', 'East'),
        ('S', 'South'),
        ('W', 'West'))

    player     = models.ForeignKey('Player')
    _round     = models.ForeignKey('Round')
    position   = models.CharField(max_length = 1, choices = POSITION_CHOICES)
    mahyong    = models.BooleanField(default = False)
    boardScore = models.PositiveIntegerField()
    gameScore  = models.IntegerField(default = 0)
    
    @staticmethod
    def calculateGameScore(playerround1, playerround2):
        # If either player is playing as East, all scores are doubled
        if (playerround1.position == 'East' or playerround2.position == 'East'):
            factor = 2
        else:
            factor = 1

        # If a player has mahyong, the worst case gamescore becomes 0
        if (playerround1.mahyong):
            score = factor * max(0,playerround1.boardScore - playerround2.boardScore)
        elif (playerround2.mahyong):
            # Change of sign because score is calculated from player 1 to player 2
            score = factor * -max(0, playerround2.boardScore - playerround1.boardScore)
        else:
            # No player has mahyong, the gamescore is simply the difference
            score = factor * (playerround1.boardScore - playerround2.boardScore)
        
        # Add scores to gamescore
        playerround1.gameScore += score
        playerround2.gameScore -= score

    def __unicode__(self):
        str_MY = 'M' if self.mahyong else ''
        str_E  = 'E' if self.position == 'E' else ''
        return str.format("{} {}{} - {} points", self.player, str_MY, str_E, self.gameScore)
