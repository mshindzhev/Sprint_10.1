import allure

import data
from methods.login_methods import LoginMethods


class TestLogin:

    @allure.title('Успешный логин пользователя')
    def test_login_success(self):
        user_login = LoginMethods.user_login(data.EMAIL, data.PASSWORD)
        assert user_login[0] == 201 and user_login[1]['user']['email'] == data.EMAIL
