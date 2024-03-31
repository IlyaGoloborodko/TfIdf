# Расчет TF-IDF
## Установка и запуск
### Основной стек:
* python 3.12
* Django 4.2.11
* django-bootstrap-v5
```
pip install requirements.txt
```

## Немного о приложении
При первом заходе в приложение нас встречает небольшое приветственное окно:
![mainpage](https://i.imgur.com/1bKu9hE.png)

Здесь мы можем нажать на кнопку "Add Document" и перейти на страницу загрузки документа:

![downloadpage](https://i.imgur.com/Y5eV0tg.png)

После загрузки ссылка на результат обработки документа появится в левом меню. При переходе по ссылке загружается таблица с 50 словами.

![listpage1](https://i.imgur.com/iXpiCjD.png)

При загрузке каждого нового документа idf всех слов обновляется:

![listpage2](https://i.imgur.com/2CXiUNQ.png)

Для наглядности загрузим документ со словами из предыдущих текстов:

![listpage3](https://i.imgur.com/cgK0cvw.png)
