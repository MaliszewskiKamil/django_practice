from django.db import models


# Create your models here.

class Container(models.Model):
    text = models.CharField(max_length=300)