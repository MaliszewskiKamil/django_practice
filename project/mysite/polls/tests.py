import datetime
import time
from django.test import TestCase
from .models import Question 
from django.utils import timezone
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


# Create your tests here.
class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)        

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), False)
        
class TestHomePage(StaticLiveServerTestCase):
    
    def setUp(self):
        self.time = timezone.now()
        self.all_questions = Question.objects.all()
        self.browser = webdriver.Chrome('/home/crypt0/programming/drivers/chromedriver')
        
    def tearDown(self):
        self.browser.close()
        
    def test_home(self):
        self.browser.get(self.live_server_url+"/polls")
        time.sleep(2)
        
        self.assertEqual(
            self.browser.find_element_by_tag_name('p').text,
            'No polls are avaiable'
        )
    def test_question_add(self):
        count_before = self.all_questions.count()
        Question.objects.create(question_text='hello', pub_date=self.time)
        self.assertNotEqual(count_before, self.all_questions.count())
        
