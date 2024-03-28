from django.shortcuts import render
from django.views.generic import ListView

from .models import Document


class MainListView(ListView):
    model = Document
    context_object_name: str = 'docs'
    template_name: str = 'tfidf/main/list.html'
    # paginate_by: int = 10
