import re
import math
from collections import defaultdict
#Используем nltk только для фильтра стоп-слов
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords


class TfIdf:
    def __init__(self):
        self.__tf_idf_dict = defaultdict(lambda: {
                                        "total_occurences": 0,
                                        "tf": {},
                                        "idf": 0,
                                        "Processed": False
                                        })
        self.__total_docs = 0

    def __words_filter(self, full_string: str) -> list:
        """
        Метод принимает строку и возвращает отфильтрованный от стоп-слов список
        """
        only_words = re.findall(r"\b\S+\b", full_string.lower())
        filtered_words = [word for word in only_words if not word in stopwords.words("english") and
                          not word in stopwords.words("russian")]
        return filtered_words

    def tf(self, text: list, doc_name: str) -> None:
        """
        Метод принимает лист и название документа. Вычисляет tf для него
        """
        if len(text) != 0:
            self.__total_docs += 1
            words_tf = defaultdict(int)
            for string in text:
                filtered_words = self.__words_filter(string)
                for word in filtered_words:
                    words_tf[word] += 1
            #Проходимся по всем ключам
            for word in words_tf:
                self.__tf_idf_dict[word]["total_occurences"] += 1
                #Мерджим два словаря
                self.__tf_idf_dict[word]["tf"] = self.__tf_idf_dict[word]["tf"] | {doc_name: words_tf[word]}
                #Помечаем слово для дальнейшей обработки при ленивом вычислении
                self.__tf_idf_dict[word]["Processed"] = True

    def __call__(self) -> tuple:
        """
        Вычисляет idf у всех еще не обработанных слов и возвращает кортеж из
        словаря
        """
        if self.__total_docs > 1:
            for elem in self.__tf_idf_dict:
                if self.__tf_idf_dict[elem]["Processed"]:
                  new_idf = round(math.log10(self.__total_docs/self.__tf_idf_dict[elem]["total_occurences"]), 3)
                  self.__tf_idf_dict[elem]["idf"] = new_idf
                  self.__tf_idf_dict[elem]["Processed"] = False
        else:
            return f"Для результата нужно обработать больше 1 документа. Сейчас {self.__total_docs}"
        return (dict(self.__tf_idf_dict), self.__total_docs)
