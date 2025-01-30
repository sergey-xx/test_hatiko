# test_hatiko

Тестовое задание Хатико

python 3.11

Для запуска требуется установка docker и docker compose.

## Запуск проекта

1. Скопировать проект на сервер
2. Переименовать файл .env.example в .env и заполнить переменные по образцу
3. В папке с проектом выполнить команду
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

## Управление конфигурациями

В проекте используется библиотека django-liveconfigs, настраивать можно тут:
/admin/liveconfigs/configrow/

## API

Получить токен:
POST /api/v1/auth/jwt/create/
```json

{
    "username": "username",
    "password": "password"
}
```
Проект реализует эндпоинт:
POST /api/v1/check-imei/

Авторизация 
```
--header 'Authorization: Bearer <YOUR API KEY>' 
```
Запрос
```json
{
    "code": "123456789012345"
}
```

Статус **201**
```json
{
  "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
  "type": "api",
  "status": "successful",
  "orderId": "",
  "service": {
    "id": 1,
    "title": "Apple Basic Info"
  },
  "amount": "0.14",
  "deviceId": "123456789012345",
  "processedAt": 41241252112,
  "properties": {
    "deviceName": "iPhone 11 Pro",
    "image": "https://sources.imeicheck.net/image.jpg",
    "imei": "123456789012345",
    "estPurchaseDate": 1422349078,
    "simLock": true,
    "warrantyStatus": "AppleCare Protection Plan",
    "repairCoverage": "false",
    "technicalSupport": "false",
    "modelDesc": "IPHONE 12 BLACK 64GB-JPN",
    "demoUnit": true,
    "refurbished": true,
    "purchaseCountry": "Thailand",
    "apple/region": "AT&T USA",
    "fmiOn": true,
    "lostMode": "false",
    "usaBlockStatus": "Clean",
    "network": "Global"
  }
}
```

Статус **401**
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```

Статус **422**
```json
{
  "errors": {
    "deviceId": [
      "The device id field is required"
    ]
  }
}
```