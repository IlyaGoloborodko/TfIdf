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

def tfidf(text, document):
    if len(text) != 0:
        words_tf = defaultdict(int)
        filtered_words = words_filter(text)
        for word in filtered_words:
            words_tf[word] += 1
    
        db_words = []
        #проходимся по всем словам из текста
        for elem in words_tf:
            #Получаем слово и обновляем поля
            word, created = Word.objects.get_or_create(word_name=elem)
            
            print(word.total_occurences)
            word.total_occurences += 1
            #Вычисляем именно десятичный логарифм
            docs_count = Document.objects.count()
            word.idf = round(math.log10(docs_count/word.total_occurences), 3)

            word.save()
            #Добавляем слово в список
            db_words.append(word)

            #Обновляем слова в промежуточной таблице
            word_doc, created = WordDocument.objects.get_or_create(word=word, document=document)
            word_doc.word_tf = words_tf[elem]
            word_doc.save()

        #Привязываем слова к документу
        document.words.add(*db_words)

        return True
    return False
    
