Для работы необходим файл settings.ini:

```
[database]
DATABASE_NAME: dbname
DATABASE_USER: dbuser
DATABASE_PASSWORD: dbpass
DATABASE_HOST: localhost
DATABASE_PORT: 3306

[security]
SECRET_KEY: key
```

Перед первым запуском нужно выполнить миграцию схемы БД:
```
python manage.py migrate
```

