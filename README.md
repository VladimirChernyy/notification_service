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

## Над проектом работал:
[Vladimir Chernyy](https://github.com/VladimirChernyy)