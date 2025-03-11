import factory

from django.contrib.auth.models import User
from snippets.models import Snippet


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')

class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet
    title = factory.Faker('sentence', nb_words=4)
    code = factory.Faker('text')
    linenos = factory.Faker('boolean')
    language = 'python'
    style = 'friendly'
    owner = factory.SubFactory(UserFactory)