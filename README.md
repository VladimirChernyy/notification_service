# Notification service

## Описание проекта:

Проект для рассылки уведомлений 


## В проекте были использованы технологии:

Python 3.11
Django REST
PostgreSQL
Celery
Redis
Docker
Gunicorn
Nginx

## Как запустить проект:

 
Клонируйте с GitHub проект и перейдите в директорию проекта.
``` 
git@github.com:VladimirChernyy/notification_service.git

cd notification_service
``` 

Перейдите директорию src:

```
cd src
```

Соберите и запустите контейнеры в фоновом режиме
```
docker compose up --build -d
```
Примените миграции
```
docker compose exec backend python manage.py migrate

```
Соберите статику
```
docker compose exec backend python manage.py collectstatic
```

Создайте суперпользователся
```
docker compose exec backend python manage.py createsuperuser
```

Остановить docker compose 
```
docker compose stop
```
## Адреса проекта:
Admin
* http://localhost:8000/admin/ 

Swagger
* http://localhost:8000/docs/ 

Celery dashboard
* http://localhost:5555/ 

## Дополнительные задания:

3 Подготовить docker-compose для запуска всех сервисов проекта одной командой

5 Сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: https://petstore.swagger.io

9 Удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.

## Над проектом работал:
[Vladimir Chernyy](https://github.com/VladimirChernyy)