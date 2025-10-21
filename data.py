# Заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {"Content-Type": "application/json"}
order_body = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "ул. Ленина, д.1",
    "metroStation": 10,
    "phone": "+7 800 355 35 35",
    "rentTime": 3,
    "deliveryDate": "2025-12-12",
    "comment": "не звонить в домофон",
    "color": ["BLACK"],
}


# Вспомогательная функция: создаёт копию тела заказа (для параметризованных тестов в будущем)
def get_order_body():
    return order_body.copy()
