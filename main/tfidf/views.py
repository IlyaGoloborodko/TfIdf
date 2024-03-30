from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .models import Document, Word
from .forms import UploadDocumentForm
from .utils import tfidf, idf_processing


class MainListView(ListView):
    model = Document
    context_object_name = 'docs'
    template_name = 'tfidf/main/list.html'
    paginate_by: int = 10

    def get_queryset(self):
        #Если есть необработанные слова, то перед выводом в них вычисляются idf
        unprocessed_words = Word.objects.all().filter(processed=False)
        if unprocessed_words:
            idf_processing(unprocessed_words)

        if 'id' in self.request.GET:
            document_id = self.request.GET.get('id', '')
            queryset = Document.objects.all().filter(id=document_id)
        else:
            queryset = Document.objects.all()
        return queryset
    

class DocumentAddView(CreateView):
    model = Document
    template_name = 'tfidf/main/documentadd.html'
    form_class = UploadDocumentForm
        
    def get_success_url(self):
        url = reverse_lazy("tfidf:document_create")
        return url

    def form_valid(self, form):
        doc_file = form.cleaned_data.get('document_file')
        if doc_file:
            b_string = doc_file.read()
            raw_txt = str(b_string, encoding='utf-8')

            tfidf(raw_txt, doc_file)

        return HttpResponseRedirect(self.get_success_url())

class MainPageView(TemplateView):
    template_name = 'tfidf/main/mainpage.html'
