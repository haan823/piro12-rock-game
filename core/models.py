from django.conf import settings
from django.db import models

GAME_CHOICES = (
    ("",""),
    ("Rock", "Rock"),
    ("Scissors", "Scissors"),
    ("Paper", "Paper"),
)

class User(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Game(models.Model):
    atk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attacker')
    dfn_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='defender')
    atk_choice = models.CharField(max_length=10, default='Rock', choices=GAME_CHOICES)
    dfs_choice = models.CharField(max_length=10, default='Rock', choices=GAME_CHOICES)
    result = models.CharField(max_length=50)