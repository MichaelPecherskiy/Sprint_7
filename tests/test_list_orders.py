from create_user import new_user
import allure
import requests
from routes import ROUTE_CREATE, ROUTE_LOGIN, ROUTE_ORDER, ROUTE_LIST_OF_ORDERS
from utils import build_url, list_of_orders_url_user
from create_order import new_order


@allure.title("получение списка заказа у курьера")
@allure.description("Этот тест проверяет список заказа у курьера")
def test_list_of_orders_id_courier():
    with allure.step("Создание нового курьера"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=new_user.auth_part()
        )
    assert response.status_code == 201
    response_json = response.json()
    assert response_json == {'ok': True}

    with allure.step("логин нового курьера"):
        response_login = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=new_user.auth_part()
    )
    assert response_login.status_code == 200
    with allure.step("Создание заказа"):
        order = requests.post(
            url=build_url(ROUTE_ORDER),
            json=new_order.order_part()
        )
    assert order.status_code == 201
    with allure.step("получение списка заказа"):
        login_user = response_login.json()
        assert 'id' in login_user
        courierId = login_user.get('id')
        get_list_response = list_of_orders_url_user(courierId)
        assert get_list_response.status_code == 200


@allure.title("Тест получение списка заказов")
@allure.description("Этот тест проверяет получение общего списка заказов")
def test_list_of_orders():
    with allure.step("вызов урлы для получения списка"):
        response_list = requests.get(
        url=build_url(ROUTE_LIST_OF_ORDERS),
    )
    with allure.step("статус код + проверка списка"):
        assert response_list.status_code == 200
        lis_orders = response_list.json()
        assert "orders" in lis_orders
