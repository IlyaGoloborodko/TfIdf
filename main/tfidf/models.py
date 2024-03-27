from django.db import models

class Document(models.Model):
    document_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.document_name
    
    class Meta:
        ordering = ['id']


class Word(models.Model):
    word_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    total_occurences = models.IntegerField(default = 0)
    idf = models.FloatField(default = 0.0)
    processed = models.BooleanField(default = False)
    documents = models.ManyToManyField(Document, through="WordDocument")

    class Meta:
        ordering = ["-idf"]
        indexes = [
            models.Index(fields=['-idf']),
        ]

    def get_documents(self):
        return "\n".join([d.document_name for d in self.documents.all()])

    def __str__(self) -> str:
        return self.word_name


class WordDocument(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    word_tf = models.IntegerField(default = 0)
