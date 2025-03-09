from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

