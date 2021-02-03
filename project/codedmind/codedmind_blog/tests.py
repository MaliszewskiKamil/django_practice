from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from .models import Article
from django.utils import timezone


# Create your tests here.

class testModels(LiveServerTestCase):
    
    def setUp(self):
        self.all_articles = Article.objects.all()        
        self.test_article = Article(title="Practical Python Course, part 1", img_path="127.0.0.1:8000/static/img/coding.jpg", article="This will be introduction part of the course. We will cover the installation process.", pub_date=timezone.now())

    def testAddArticle(self):
        countBeforeAdding = self.all_articles.count()
        self.test_article.save()
        self.assertNotEqual(self.all_articles.count(), countBeforeAdding)

        
    def testDeleteArticle(self):
        countBeforeDeleting = self.all_articles.count()
        self.test_article.save()
        self.assertEqual(1, self.all_articles.count())
        Article(id=1).delete()
        self.assertNotEqual(self.all_articles.count(), countBeforeDeleting)
