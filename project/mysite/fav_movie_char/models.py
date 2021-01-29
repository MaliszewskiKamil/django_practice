from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    
class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    char_name = models.CharField(max_length=100, default='Bob')
    votes = models.IntegerField(default=0)
