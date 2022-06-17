import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from .models import Question

# Create your tests here.
# Generalmente se testean los modelos y vistas de una app

# Test de Modelos 
class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor alumno del IMC?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) #verificamos si es Falso

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index")) #Hace request hhtp a la url del index y lo guardamos en la variable
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])