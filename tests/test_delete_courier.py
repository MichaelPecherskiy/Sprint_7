from create_user import new_user
import requests
from routes import ROUTE_CREATE, ROUTE_LOGIN
from utils import build_url, courier_delete
import allure


@allure.title("Тест удаление курьера")
@allure.description("Этот тест проверяет удаление курьера")
def test_delete_courier():
    with allure.step("Создание нового курьера"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=new_user.auth_part()
        )
        assert response.status_code == 201
        response_json = response.json()
        assert response_json == {'ok': True}
    with allure.step("Логин нового курьера"):
        response_login = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=new_user.auth_part()
        )
    assert response_login.status_code == 200
    response_login_json = response_login.json()
    with allure.step("Удаление курьера"):
        courier_id = response_login_json.get('id')
        assert courier_id is not None, "Курьера с таким id нет"
        delete_response = courier_delete(courier_id)
        assert delete_response.status_code == 200
        delete_response_json = delete_response.json()
        assert delete_response_json == {'ok': True}
