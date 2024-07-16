import requests
from create_user import login_user, login_user_empty_fields, login_unknown, login_incorrect_password, \
    login_incorrect_email
from routes import ROUTE_LOGIN
from utils import build_url
import allure


@allure.title("Тест логин юзера")
@allure.description("Этот тест проверяет логин юзера")
def test_login_user():
    with allure.step("логин"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=login_user.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 200
    with allure.step("проверка id в ответе json"):
        response_json = response.json()
        assert response_json == {"id": 348723}


@allure.title("Тест попытка логин с пропущенными полями")
@allure.description("Этот тест проверяет попытку залогиниться с пропущенными полями")
def test_login_with_missing_field():
    with allure.step("подборка ввода данных json"):
        data = {
            "login": login_user.login,
        }
    with allure.step("логин"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=data
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 400
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Недостаточно данных для входа'


@allure.title("Тест создание курьера с пустыми данными в json")
@allure.description("Этот тест проверяет создание курьера с пустыми полями для заполнения")
def test_login_with_empty_fields():
    with allure.step("создание пользователя с пустыми полями"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=login_user_empty_fields.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 400
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Недостаточно данных для входа'


@allure.title("Тест попытка логина неизвестного пользователя ")
@allure.description("Этот тест проверяет логин несуществующего пользователя")
def test_login_unknown():
    with allure.step("создание неизвестного пользака и логин"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=login_unknown.auth_part()
        )
    with allure.step("проверка статус кода"):
        assert response.status_code == 404
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Учетная запись не найдена'


@allure.title("Тест логин пользователя с неверным паролем")
@allure.description("Этот тест проверяет логин пользака с неверным паролем")
def test_login_incorrect_password_login():
    with allure.step("создание пользователя с неверным паролем и логин"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=login_incorrect_password.auth_part()
        )
    with allure.step("статус кода"):
        assert response.status_code == 404
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Учетная запись не найдена'
    with allure.step("создание пользователя с некорректным email и логин"):
        response = requests.post(
            url=build_url(ROUTE_LOGIN),
            json=login_incorrect_email.auth_part()
        )
    with allure.step("статус кода"):
        assert response.status_code == 404
    with allure.step("проверка message"):
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Учетная запись не найдена'