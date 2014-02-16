from django.db import models

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

    def __unicode__(self):
        return self.fullname()

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
    date_started = models.DateField()
    players      = models.ManyToManyField('Player')

class Round(models.Model):
    players = models.ManyToManyField('Player', through='PlayerRound')
    game    = models.ForeignKey('Game')

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
    gameScore  = models.IntegerField()
