# Проект vps_servers
Тестовое задание на основе требований, описанных в вакансии.

# Установка и развертывание проекта на локальном сервере
1. Склонируйте репозиторий. 
2. Создайте и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости из requirements.txt `pip install -r requirements.txt`
4. В директории vps_servers/vps_servers создайте .env-файл со значениями 
SECRET_KEY, DEBUG и ALLOWED_HOSTS
5. В директории vps_servers выполните миграции `python manage.py migrate`
6. Запустите локальный сервер `python manage.py runserver`

# Примеры запросов к сервису:
Можно протестировать через Postman
1. GET-запрос к https://127.0.0.1:8000/servers/ - перечень всех серверов
2. POST-запрос к http://127.0.0.1:8000/servers/ - создание сервера
Тело запроса:
```
{
    "cpu": 2,
    "ram": 1024,
    "hdd": 1024,
    "status": "Started"
}
```
3. GET-запрос к http://127.0.0.1:8000/servers/?search=rdcf8po7fz2ed8c9 - получение конкретного сервера по его uid
4. PATCH-запрос к http://127.0.0.1:8000/servers/1/update_status/- изменение статуса сервера по его pk
Тело запроса:
```
{
    "status": "Started"
}
```

# Автор:
Кошурин Артём
