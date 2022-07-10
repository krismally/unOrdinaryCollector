from unicodedata import name
from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    ability_score = models.FloatField()

    def __str__(self):
        return self.name

    