from django.db import models

# Create your models here.
default_article="Hello, this is a default, empty article"

class Article(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    img_path = models.CharField(max_length=150, default='img/default.png')
    article = models.TextField(default=default_article, null=False)

class Keywords(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, null=False, default="none")