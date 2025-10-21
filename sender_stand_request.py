# Импорт необходимых модулей
from configuration import (
    URL_SERVICE,
    CREATE_ORDER_PATH,
    GET_ORDER_BY_TRACK_PATH,
)  # Модуль с настройками URL и путей API
import requests  # Библиотека для выполнения HTTP-запросов


# Функции для создания нового заказа
# Выполнение POST-запроса на создание заказа
def create_order(body):
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH, json=body)


# Выполнение GET-запроса для получения заказа по трек-номеру
# Параметр track_number должен быть числом
def get_order_by_track(track_number):
    return requests.get(
        URL_SERVICE + GET_ORDER_BY_TRACK_PATH, params={"t": track_number}
    )
