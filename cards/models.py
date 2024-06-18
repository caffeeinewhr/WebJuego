# models.py
from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    cost = models.IntegerField()
    image_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
