from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from forum_app.models import Like, Question

class LikeTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other = User.objects.create_user(username='other', password='other-pw')
        self.question = Question.objects.create(title='Test Question', content='Test Content', author=self.other, category='frontend')
        self.like = Like.objects.create(user=self.user, question=self.question)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_likes(self):
        url = reverse('like-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_like(self):
    #     self.client.logout()
    #     self.client.login(username='other', password='other-pw')
    #     q2 = Question.objects.create(title='Q2', content='New content', author=self.other, category='frontend')
    #     url = reverse('like-list')
    #     data = {
    #         "question": q2.id
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['user'], self.user.id)
