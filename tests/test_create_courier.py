import requests
from create_user import base_user, new_user, user_with_empty_fields
from routes import ROUTE_CREATE
from utils import build_url
import allure


@allure.title("Тест создание курьера")
@allure.description("Этот тест проверяет создание курьера")
def test_create_courier():
    with allure.step("создание нового пользователя"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=new_user.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 201
    with allure.step("проверка ответа {'ok': True}"):
        response_json = response.json()
        assert response_json == {'ok': True}


@allure.title("Тест создание курьера с имеющимся логином")
@allure.description("Этот тест проверяет создание курьера с имеющимся логином")
def test_create_courier_with_existing_login():
    with allure.step("создание нового пользователя с имеющимся логином"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=base_user.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 409
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Этот логин уже используется. Попробуйте другой.'


@allure.title("Тест создание дубликата курьера")
@allure.description("Этот тест проверяет создание дубликата курьера")
def test_create_duplicate_courier():
    with allure.step("создание нового курьера"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=new_user.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 201
    with allure.step("проверка message"):
        response_json = response.json()
        assert response_json == {'ok': True}
    with allure.step("создание дубликата курьера"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=new_user.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 409
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Этот логин уже используется. Попробуйте другой.'


@allure.title("Тест создание курьера с пропущенными полями в json")
@allure.description("Этот тест проверяет создание курьера с пропущенными полями в json")
def test_create_courier_with_missing_field():
    with allure.step("выбираем кол-во полей которые будем передавать"):
        data = {
            "login": new_user.login,
            "firstName": new_user.firstName
        }
    with allure.step("попытка создания курьера"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=data
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 400
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Недостаточно данных для создания учетной записи'


@allure.title("Тест создание курьера с пустыми данными в json")
@allure.description("Этот тест проверяет создание курьера с пустыми полями для заполнения")
def test_create_courier_with_empty_fields():
    with allure.step("создание курьера с пустыми данными в json"):
        response = requests.post(
            url=build_url(ROUTE_CREATE),
            json=user_with_empty_fields.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 400
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Недостаточно данных для создания учетной записи'


