import allure
import pytest

import data
from methods.ad_methods import AdMethods


class TestAd:

    @allure.title('Успешный логин пользователя')
    def test_login_success(self):
        user_login = AdMethods.user_login(data.EMAIL, data.PASSWORD)
        assert user_login[0] == 201 and user_login[1]['user']['email'] == data.EMAIL