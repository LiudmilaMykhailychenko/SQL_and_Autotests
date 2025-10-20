# Людмила Михайличенко, 36-я когорта — Финальный проект. Инженер по тестированию плюс
# Импортируем необходимые модули
import pytest
from data import get_order_body  # Функция для получения тестовых данных заказа
from sender_stand_request import (
    create_order,
    get_order_by_track,
)  # Функции отправки API-запросов


# ОСНОВНОЙ ТЕСТ - Проверяем, что по треку заказа можно получить данные о заказе
def test_create_and_get_order():
    # ШАГ 1: Подготовка и отправка запроса на создание заказа
    order_body = get_order_body()  # Получаем тестовые данные из data.py
    create_response = create_order(order_body)  # Отправляем POST-запрос

    # Проверяем, что заказ создан успешно (статус 201)
    assert (
        create_response.status_code == 201
    ), f"Ошибка при создании заказа. Статус: {create_response.status_code}"

    # Извлекаем трек-номер из ответа
    track = create_response.json().get("track")
    # Убеждаемся, что трек — целое положительное число (по спецификации API)
    assert isinstance(track, int) and track > 0, f"Некорректный трек-номер: {track}"

    # ШАГ 2: Получение заказа по трек-номеру
    get_response = get_order_by_track(
        track
    )  # Отправляем GET-запрос с параметром t=track

    # Проверяем, что сервер вернул успешный ответ (статус 200)
    assert (
        get_response.status_code == 200
    ), f"Получен статус: {get_response.status_code}"

    # ШАГ 3: Валидация структуры и содержимого ответа
    response_data = get_response.json()

    # Проверка: в корне ответа должен быть ключ "order"
    assert "order" in response_data, "В ответе отсутствует обязательный ключ 'order'"
    order = response_data["order"]
    assert isinstance(order, dict), "Поле 'order' должно быть объектом (словарем)"

    # Список обязательных полей в объекте 'order' и их ожидаемые типы данных
    required_fields = {
        "id": int,
        "firstName": str,
        "lastName": str,
        "address": str,
        "metroStation": str,
        "phone": str,
        "rentTime": int,
        "deliveryDate": str,
        "track": int,
        "status": int,
        "color": list,
        "comment": str,
        "cancelled": bool,
        "finished": bool,
        "inDelivery": bool,
        "createdAt": str,
        "updatedAt": str,
    }

    # Проверяем каждое поле: есть ли оно и правильного ли типа
    for field, expected_type in required_fields.items():
        assert field in order, f"В объекте 'order' отсутствует поле: '{field}'"
        assert isinstance(
            order[field], expected_type
        ), f"Поле '{field}': ожидалось {expected_type.__name__}, получено {type(order[field]).__name__}"

    # Если все проверки прошли — тест успешен
    print(f"Тест пройден. Заказ с треком {track} успешно создан и получен.")
