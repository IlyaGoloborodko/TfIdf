from django.utils.functional import SimpleLazyObject
from .models import Document

def get_documents(request):
    if not hasattr(request, '_cached_document'):
        request._cached_document = Document.objects.all()
    return request._cached_document

class DocumentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.document = SimpleLazyObject(lambda: get_documents(request))
        response = self.get_response(request)
        return response
