from django.test import TestCase
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.models import Snippet
from snippets.factories import SnippetFactory, UserFactory

class SnippetSerializerTest(TestCase):
    def setUp(self):
        self.snippet = SnippetFactory()
    def test_snippet_serialization(self):
        serializer = SnippetSerializer(instance=self.snippet)
        data = serializer.data
        self.assertEqual(data["title"], self.snippet.title)
        self.assertEqual(data["code"], self.snippet.code)
        self.assertEqual(data["linenos"], self.snippet.linenos)
        self.assertEqual(data["language"], self.snippet.language)
        self.assertEqual(data["style"], self.snippet.style)
        self.assertEqual(data["owner"], self.snippet.owner.username)
    def test_snippet_deserialization_valid_data(self):
        valid_data = {
            "title": "New Snippet",
            "code": "print('Hello, world!')",
            "linenos": True,
            "language": "python",
            "style": "friendly",
        }
        serializer = SnippetSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        snippet = serializer.save(owner=self.snippet.owner)
        self.assertEqual(snippet.title, valid_data['title'])
    def test_snippet_deserialization_invalid_data(self):
        """Test handling of invalid data."""
        invalid_data = {"title": "", "code": ""}  # Missing required fields
        serializer = SnippetSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("code", serializer.errors)  # Expect validation error

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.snippet = SnippetFactory(owner=self.user)
    def test_user_serialization(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['username'], self.user.username)
        self.assertIn(self.snippet.id, data['snippets'])
        