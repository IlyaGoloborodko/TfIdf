import re
import math
from collections import defaultdict
#Используем nltk только для фильтра стоп-слов
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

from .models import Word, Document, WordDocument

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

        num_of_words = len(words_count)

    
        db_words = []
        #проходимся по всем словам из текста
        for elem in words_count:
            #Получаем слово и обновляем поля
            word, created = Word.objects.get_or_create(word_name=elem)
            word.total_occurences += 1
            # Помечаем слово как False, чтобы в дальнейшем обновить у него idf
            word.processed = False
            word.save()
            #Добавляем слово в список
            db_words.append(word)
            #Обновляем слова в промежуточной таблице
            word_doc, created = WordDocument.objects.get_or_create(word=word, document=document)
            word_doc.word_tf = round(words_count[elem]/num_of_words, 3)

            word_doc.save()

        #Привязываем слова к документу
        document.words.add(*db_words)

        return True
    return False

def idf_processing(words):
    """
    Ленивое вычисление idf только при вызове всех значений.
    Вызывается только после перехода на главную страницу
    """
    for word in words:
        #Вычисляем именно десятичный логарифм
        docs_count = Document.objects.count()
        word.idf = round(math.log10(docs_count/word.total_occurences), 3)
        word.processed = True
        word.save()

    
