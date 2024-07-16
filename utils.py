from routes import API_HOST, ROUTE_LIST_OF_ORDERS_USER
from routes import ROUTE_DELETE_COURIER
import requests
import random
import string
import allure



@allure.step("создание урлы")
def build_url(path):
    return API_HOST + path


@allure.step("генерация рандомной строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("генерация имени")
def generate_first_name():
    return generate_random_string(10)


@allure.step("генерация фамилии")
def generate_last_name():
    return generate_random_string(10)


@allure.step("метод удаления курьера")
def courier_delete(courier_id: int):
    url = f"{build_url(ROUTE_DELETE_COURIER)}/{courier_id}"
    delete = requests.delete(url)
    return delete


@allure.step("метод создания урлы для заказов курьера")
def list_of_orders_url_user(order_id: int):
    url = f'{build_url(ROUTE_LIST_OF_ORDERS_USER)}{int(order_id)}'
    print(f"URL for listing orders: {url}")  # Добавлено для вывода URL
    list_orders = requests.get(url)
    return list_orders


@allure.step("метод создания урлы заказов")
def list_of_orders_url(order_id: int):
    url = f'{build_url(ROUTE_LIST_OF_ORDERS_USER)}{int(order_id)}'
    print(f"URL for listing orders: {url}")  # Добавлено для вывода URL
    list_orders = requests.get(url)
    return list_orders
