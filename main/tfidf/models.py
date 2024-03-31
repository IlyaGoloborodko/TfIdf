from django.db import models


class Word(models.Model):
    word_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    total_occurences = models.IntegerField(default=0)
    idf = models.FloatField(default=0.0)

    class Meta:
        ordering = ["-idf"]
        indexes = [
            models.Index(fields=['-idf']),
        ]

    def __str__(self) -> str:
        return self.word_name
    
class Document(models.Model):
    document_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    words = models.ManyToManyField(Word, through="WordDocument")
    document_file = models.FileField(upload_to='documents/', blank=False, null=False, default=None)

    def get_words(self):
        return "\n".join([d.word_name for d in self.words.all()])

    def __str__(self) -> str:
        return self.document_name
    
    class Meta:
        ordering = ['id']

class WordDocument(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    word_tf = models.FloatField(default = 0.0)
