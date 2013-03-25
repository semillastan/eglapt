from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField("Name", max_length=64)
    description = models.TextField("Description")
    game_id = models.CharField("Game ID", max_length=8)
    api_key = models.CharField("API Key", max_length=24)
    public = models.BooleanField(default=True)
    
    date_created = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True)

    class Meta:
	unique_together = ('game_id','api_key')

TIME_UNIT = (
    ('seconds','seconds'),
    ('minutes','minutes'),
    ('hours','hours'),
)

class GameLevel(models.Model):
    game = models.ForeignKey(Game)
    level = models.CharField("Level", max_length=32)
    difficulty = models.CharField("Difficulty", max_length=32)
    max_score = models.PositiveIntegerField(default=0)
    max_playing_time_value = models.PositiveIntegerField(default=0)
    max_playing_time_unit = models.CharField("Time Unit", choices=TIME_UNIT, max_length=8)

    date_created = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True)

class APT(models.Model):
    user = models.ForeignKey(User, related_name="user")
    game_level = models.ForeignKey(GameLevel)
    date_played = models.DateField(blank=True, null=True)
    total_score = models.PositiveIntegerField(default=0)
    playing_time = models.TimeField()

    date_added = models.DateField(blank=True, null=True)
    added_by = models.ForeignKey(User, related_name="added_by", blank=True, null=True)
