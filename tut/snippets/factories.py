import factory
from snippets.models import Snippet

class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet
    title = factory.Faker('sentence', nb_words=4)
    code = factory.Faker('text')
    linenos = factory.Faker('boolean')
    language = 'python'
    style = 'friendly'
        