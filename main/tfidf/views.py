from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document
from .forms import UploadDocumentForm


class MainListView(ListView):
    model = Document
    context_object_name = 'docs'
    template_name = 'tfidf/main/list.html'
    # paginate_by: int = 10



class DocumentAddView(CreateView):
    model = Document
    template_name = 'tfidf/main/documentadd.html'
    form_class = UploadDocumentForm
        
    def get_success_url(self):
        url = reverse_lazy("tfidf:main_list")
        return url

    # def form_valid(self, form):
    #     print(form)
