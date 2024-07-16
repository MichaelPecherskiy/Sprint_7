import pytest
import requests
import allure
from routes import ROUTE_ORDER
from utils import build_url
from faker import Faker
from create_order import Order
fake = Faker()


@allure.title("Тест создание заказа")
@allure.description("Этот тест проверяет создание заказа")
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], []])
def test_create_order(color):
    with allure.step("Создание нового заказа с данными для параметризации в color "):
        new_order = Order(
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            address=fake.address(),
            metroStation=4,
            phone=fake.phone_number(),
            rentTime=5,
            deliveryDate=fake.date(),
            comment="Leave at the door",
            color=color
        )
    with allure.step("Создание создание заказа"):
        response = requests.post(
            url=build_url(ROUTE_ORDER),
            json=new_order.order_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 201
    with allure.step("проверка track в json ответе"):
        response_json = response.json()
        assert 'track' in response_json
