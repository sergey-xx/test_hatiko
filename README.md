# test_hatiko

Тестовое задание Хатико

python 3.11

Для запуска требуется установка docker и docker compose.

1. Скопировать проект на сервер
2. переименовать файл .env.example в .env и заполнить переменные
3. в папке с проектом выполнить команду
```
sudo docker compose up -d
```
4. Cоздать пользователя для входа в админ-панель
```
 sudo docker compose exec admin_panel python manage.py createsuperuser
```
После чего ввести имя, почту (можно выдуманную, но валидную) и пароль для админки

Загрузить базовые конфигурации
```
sudo docker compose exec admin_panel python manage.py load_config
```

## Пересборка контейнера
```
sudo docker compose down
sudo docker compose up -d --build
```