from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document
from .forms import UploadDocumentForm
from .utils import tfidf


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

    def form_valid(self, form):
        doc_file = form.cleaned_data.get('document_file')
        if doc_file:
            b_string = doc_file.read()
            raw_txt = str(b_string, encoding='utf-8')

            db_doc = Document.objects.create(document_name=doc_file, document_file=doc_file)
            tfidf(raw_txt, db_doc)

        return HttpResponseRedirect(self.get_success_url())
