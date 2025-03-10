from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from snippets.factories import SnippetFactory
from snippets.models import Snippet


# Create your tests here.
class SnippetViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.snippet = SnippetFactory()
    def test_get_snippet_list(self):
        response = self.client.get('/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
    def test_create_snippet(self):
        data = {
            "title": "Test Snippet",
            "code": "print('Hello, World!')",
            "linenos": True,
            "language": "python",
            "style": "friendly",
        }
        response = self.client.post('/snippets/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 2)
    def test_get_snippet_detail(self):
        response = self.client.get(f'/snippets/{self.snippet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], self.snippet.title)
    def test_update_snippet(self):
        updated_data = {
            "title": "Updated Title",
            "code": self.snippet.code,
            "linenos": self.snippet.linenos,
            "language": self.snippet.language,
            "style": self.snippet.style,
        }
        response = self.client.put(f'/snippets/{self.snippet.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, 'Updated Title')
    def test_delete_snippet(self):
        response = self.client.delete(f'/snippets/{self.snippet.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Snippet.objects.filter(id=self.snippet.id).exists())
        