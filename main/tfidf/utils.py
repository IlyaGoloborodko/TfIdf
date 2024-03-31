import re
import math
from collections import defaultdict
#Используем nltk только для фильтра стоп-слов
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

from .models import Word, Document, WordDocument


def idf_processing(words):
    docs_count = Document.objects.count()
    for i in range(len(words)):
        #Вычисляем именно десятичный логарифм
        words[i].idf = round(math.log10(docs_count/words[i].total_occurences), 7)
    Word.objects.bulk_update(words, ["idf"])

def words_filter(full_string: str) -> list:
    """
    Метод принимает строку и возвращает отфильтрованный от
    стоп-слов и лишних символов список
    """
    only_words = re.findall(r"\b\S+\b", full_string.lower())
    filtered_words = [word for word in only_words if
                        not word in stopwords.words("english") and
                        not word in stopwords.words("russian")]
    return filtered_words

def tfidf(text, doc_file):
    if len(text) != 0:
        words_count = defaultdict(int)
        filtered_words = words_filter(text)
        if filtered_words:
            document = Document.objects.create(document_name=doc_file, document_file=doc_file)
        else:
            return False
        for word in filtered_words:
            words_count[word] += 1

        #Заносим слова в бд, перед этим сначала проверяя их наличие там
        existing_words = set(Word.objects.values_list('word_name', flat=True))
        words_obj = [Word(word_name=elem) for elem in words_count if
                                            elem not in existing_words]          
        Word.objects.bulk_create(words_obj, ignore_conflicts=True)
        words = Word.objects.filter(word_name__in=words_count)

        for i in range(len(words)):
            words[i].total_occurences += 1

        Word.objects.bulk_update(words, ["total_occurences"])

        #Заполняем промежуточную
        word_doc_obj = [WordDocument(word=elem, document=document) for elem in words]
        WordDocument.objects.bulk_create(word_doc_obj, ignore_conflicts=True)
        word_docs = WordDocument.objects.filter(word__in=words, document=document)

        num_of_words = len(words_count)
        for i in range(len(word_docs)):
            elem_name = word_docs[i].word.word_name
            word_docs[i].word_tf = round(words_count[elem_name]/num_of_words, 7)

        WordDocument.objects.bulk_update(word_docs, ["word_tf"])

        #Обновляем idf
        unprocessed_words = Word.objects.all()
        if unprocessed_words:
            idf_processing(unprocessed_words)

        return True
    return False



    
