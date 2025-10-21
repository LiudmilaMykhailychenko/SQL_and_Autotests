# Людмила Михайличенко, 36-я когорта — Финальный проект. Инженер по тестированию плюс
# РАСШИРЕННЫЙ ТЕСТ: валидация структуры и типов полей в ответе заказа
# Импорт необходимых модулей
import pytest
from data import get_order_body  # Функция для получения тестовых данных заказа
from sender_stand_request import create_order, get_order_by_track  # Функции отправки API-запросов


def test_order_response_structure():
    # Получение тестовых данных из data.py
    order_body = get_order_body()

    # Создание заказа
    create_response = create_order(order_body)

    # Проверка, что код ответа равен 201
    assert create_response.status_code == 201

    # Получение трек-номера из ответа
    track = create_response.json()["track"]

    # Проверка, что трек — целое положительное число
    assert isinstance(track, int)
    assert track > 0

    # Получение заказа по треку
    get_response = get_order_by_track(track)

    # Проверка, что сервер вернул успешный ответ (статус 200)
    assert get_response.status_code == 200

    # Получение тела ответа
    response_data = get_response.json()

    # Проверка, что в ответе есть ключ "order"
    assert "order" in response_data

    # Получение объекта заказа
    order = response_data["order"]

    # Проверка, что объект "order" является словарём
    assert isinstance(order, dict)

    # Проверка наличия и типа каждого обязательного поля в объекте "order"

    # Проверка поля "id"
    assert "id" in order
    assert isinstance(order["id"], int)

    # Проверка поля "firstName"
    assert "firstName" in order
    assert isinstance(order["firstName"], str)

    # Проверка поля "lastName"
    assert "lastName" in order
    assert isinstance(order["lastName"], str)

    # Проверка поля "address"
    assert "address" in order
    assert isinstance(order["address"], str)

    # Проверка поля "metroStation"
    assert "metroStation" in order
    assert isinstance(order["metroStation"], str)

    # Проверка поля "phone"
    assert "phone" in order
    assert isinstance(order["phone"], str)

    # Проверка поля "rentTime"
    assert "rentTime" in order
    assert isinstance(order["rentTime"], int)

    # Проверка поля "deliveryDate"
    assert "deliveryDate" in order
    assert isinstance(order["deliveryDate"], str)

    # Проверка поля "track"
    assert "track" in order
    assert isinstance(order["track"], int)

    # Проверка поля "status"
    assert "status" in order
    assert isinstance(order["status"], int)

    # Проверка поля "color"
    assert "color" in order
    assert isinstance(order["color"], list)

    # Проверка поля "comment"
    assert "comment" in order
    assert isinstance(order["comment"], str)

    # Проверка поля "cancelled"
    assert "cancelled" in order
    assert isinstance(order["cancelled"], bool)

    # Проверка поля "finished"
    assert "finished" in order
    assert isinstance(order["finished"], bool)

    # Проверка поля "inDelivery"
    assert "inDelivery" in order
    assert isinstance(order["inDelivery"], bool)

    # Проверка поля "createdAt"
    assert "createdAt" in order
    assert isinstance(order["createdAt"], str)

    # Проверка поля "updatedAt"
    assert "updatedAt" in order
    assert isinstance(order["updatedAt"], str)