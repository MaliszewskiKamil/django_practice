from django.db import models
from django.utils import timezone

# Create your models here.
default_article="Hello, this is a default, empty article"

class Article(models.Model):
    title = models.CharField(max_length=70, default="Blog title")
    img_path = models.CharField(max_length=150, default='img/default.png', unique=True)
    article = models.TextField(default=default_article, null=False)
    pub_date = models.DateTimeField('date_published', default=timezone.now)
    
    
class Keywords(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, null=False, default="none")

    
