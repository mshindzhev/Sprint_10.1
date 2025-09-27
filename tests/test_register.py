import allure
import pytest

import data
from methods.register_methods import RegisterMethods


class TestRegister:

    @allure.title('Успешная регистрация нового пользователя')
    def test_register_unique_user(self, create_user):
        assert create_user[0] == 201 and create_user[1]['user']

    @allure.title('Регистрация пользователя с неуникальными данными')
    def test_register_not_unique_user(self):
        not_unique_user = RegisterMethods().user_registration(data.EMAIL, data.PASSWORD, False)
        assert not_unique_user[0] == 400 and not_unique_user[1]['message'] == data.MASSAGE_FOR_NOT_UNIQUE_USER
