from django.shortcuts import render
from django.views.generic import ListView

from .models import Word


class MainListView(ListView):
    model = Word
    context_object_name: str = 'data'
    template_name: str = 'tfidf/main/list.html'

