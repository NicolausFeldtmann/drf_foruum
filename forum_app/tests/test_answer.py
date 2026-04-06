from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from forum_app.models import Answer, Question

class AnswerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.question = Question.objects.create(title='Test Question', content='Test Content', author=self.user, category='frontend')
        self.answer = Answer.objects.create(content='Existing answer', author=self.user, question=self.question)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_answer(self):
        url = reverse('answer-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_answer(self):
        url = reverse('answer-list-create')
        data = {
            "content": "Content1",
            "question": self.question.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'], self.answer.id)

    def test_detail_answer(self):
        url = reverse('answer-detail', kwargs={'pk': self.answer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.answer.content)