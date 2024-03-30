from django import forms
from .models import Document

class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["document_file", "document_name"]
