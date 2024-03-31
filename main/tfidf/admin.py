from django.contrib import admin
from .models import Document, Word, WordDocument


class WordDocumentInline(admin.TabularInline):
    model = WordDocument
    extra = 1

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['document_name', 'slug', 'get_words']
    prepopulated_fields = {'slug': ('document_name',)}
    raw_id_fields = ['words']
    inlines = (WordDocumentInline,)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['word_name', 'slug', 'total_occurences',
                    'idf']
    prepopulated_fields = {'slug': ('word_name',)}
    inlines = (WordDocumentInline,)
