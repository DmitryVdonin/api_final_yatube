# api_final
### Описание
API социальной сети Yatube. Позволяет работать с API социальной сети Yatube: создавать и получать посты,
подписываться на авторов и получать список своих подписок, получать список существующих сообществ и их описания.
### Технологии
- Python 3.7
- django 2.2.16
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
- djoser 2.1.0
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполните миграции. В папке с файлом manage.py выполните команду:
```
 python3.manage.py migtate (windows: py.manage.py migtate)
 ```
- Запустите сервер разработчика. В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver (windows: py manage.py runserver)
```
### Администрирование и особенности
- Для администрирования проекта создайте суперпользователя. В папке с файлом manage.py выполните команду:
```
python3 manage.py createsuperuser (windows: py manage.py createsuperuser)
```
- Админ-зона расположена по относительному адреу /admin/
- Создание групп в проекте возможно только для администратора в админ-зоне
### Работа с API
- Получите токен для суперпользователя отправив post запрос на относительный эндпоинт api/v1/jwt/create/, передав username и password
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/jwt/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "password"
}'
```
- Примеры запросов для получения поста/списка постов
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1/' \
--header 'Authorization: Bearer <ваш токен>' \
--data-raw ''
```
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer <ваш токен>' \
--data-raw ''
```
- Пример post запроса для создания поста
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer <ваш токен>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "первый пост"
}'
```
- Полный список возможных эндпоинтов и видов запросов доступен по относительному эндпоинту redoc/

### Авторы
Дмитрий Вдонин


