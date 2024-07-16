from dataclasses import dataclass
from faker import Faker
import allure
fake = Faker()


@allure.step("создание заказа")
@dataclass
class Order:
    firstName: str
    lastName: str
    address: str
    metroStation: int
    phone: str
    rentTime: int
    deliveryDate: str
    comment: str
    color: [str]

    def order_part(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "address": self.address,
            "metroStation": self.metroStation,
            "phone": self.phone,
            "rentTime": self.rentTime,
            "deliveryDate": self.deliveryDate,
            "comment": self.comment,
            "color": self.color
        }


new_order = Order(
    firstName="Naruto",
    lastName="Uchiha",
    address=fake.address(),
    metroStation=4,
    phone=fake.phone_number(),
    rentTime=5,
    deliveryDate=fake.date(),
    comment="Saske, come back to Konoha",
    color=[
        "BLACK"
    ]
)
