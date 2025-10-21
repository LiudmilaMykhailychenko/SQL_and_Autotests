# Людмила Михайличенко, 36-я когорта — Финальный проект. Инженер по тестированию плюс
# ОСНОВНОЙ ТЕСТ: проверка, что по треку заказа можно получить данные о заказе
# Импорт необходимых модулей
import pytest
from data import get_order_body  # Функция для получения тестовых данных заказа
from sender_stand_request import create_order, get_order_by_track  # Функции отправки API-запросов


def test_create_and_get_order():
    # Получение тестовых данных из data.py
    order_body = get_order_body()

    # Создание заказа
    create_response = create_order(order_body)  

    # Проверка, что заказ создан успешно (статус 201)
    assert create_response.status_code == 201
    
    # Извлечение трек-номера из ответа
    track = create_response.json().get("track")
    # Проверка, что трек — целое положительное число (по спецификации API)
    assert isinstance(track, int)
    assert track > 0

    #Получение заказа по трек-номеру
    get_response = get_order_by_track(track)

    # Проверка, что сервер вернул успешный ответ (статус 200)
    assert get_response.status_code == 200
