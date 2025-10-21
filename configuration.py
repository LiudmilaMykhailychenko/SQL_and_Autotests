# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = (
    "https://179c2c02-8075-4e35-bd08-6e07607e86c7.serverhub.praktikum-services.ru/"
)

# Пути API
CREATE_ORDER_PATH = "/api/v1/orders"  # эндпоинт для создания заказа
GET_ORDER_BY_TRACK_PATH = (
    "/api/v1/orders/track"  # эндпоинт для получения заказа по его номеру
)
