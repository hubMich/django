#biblioteka standarodwa
import datetime

#biblioteki zainstalowane
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

#biblioteki z projektu
from pools.models import Question

# Create your tests here.
# pytest
# BDD

def concatente_numbers(a:int, b: int) -> str:
    return str(a) + str(b)
#mypy - static type checkout

def create_question(question_text, days):
    """
    create question with given question_text and pub_data that is n days of offset to now (negative and positive values)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_data=time)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_feature_question(self):
        """
        was_published_recently - return false for question whose pub_data is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_data=time)
        self.assertIs(future_question.was_published_recently, False)

    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_data=time)
        self.assertIs(past_question.was_published_recently, False)

    def test_was_published_recently_with_recently_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recently_question = Question(pub_data=time)
        self.assertIs(recently_question.was_published_recently, True)

class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        future_question = create_question("test", days=2)
        url = reverse("pools:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question("test", days=-2)
        url = reverse("pools:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,past_question.question_text)