from dataclasses import dataclass
from faker import Faker
from typing import Optional
import allure
from utils import generate_first_name
fake = Faker()


@allure.step("создание пользователя")
@dataclass
class User:
    login: str
    password: str
    firstName: Optional[str] = None

    def auth_part(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.firstName
        }


new_user = User(
    login=fake.email(),
    password=fake.password(),
    firstName=generate_first_name()
)

base_user = User(
    login="ninja",
    password="1234",
    firstName="saske"
)

user_with_empty_fields = User(
    login="",
    password="",
    firstName="saske"
)

login_user = User(
    login="ninja_m",
    password="1234",
)

login_user_empty_fields = User(
    login="ninja_m",
    password="",
)

login_unknown = User(
    login="xxx",
    password="123321"
)

login_incorrect_password = User(
    login="ninja_m",
    password="123321"
)

login_incorrect_email = User(
    login="ninja_m_m",
    password="1234"
)
