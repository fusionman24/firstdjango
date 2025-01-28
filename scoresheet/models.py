from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

# Create your models here.
class Score(models.Model):
        # judge
        # startup
        # eureka id
        # pitch_deck = models.CharField(max_length=255)
        startup_idea = models.CharField(max_length=10)
        target_market = models.CharField(max_length=10)
        growth_potential = models.CharField(max_length=10)
        revenue_model = models.CharField(max_length=10)
        stage_of_startup = models.CharField(max_length=10)
        team_members = models.CharField(max_length=10)
        # total_score = models.CharField(max_length=255)
        feedback = models.TextField()

def __str__(self):
        return f"Score for {self.startup_idea}"