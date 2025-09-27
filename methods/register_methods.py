import allure
import requests

import data
from helpers import generate_data_for_registration


class RegisterMethods:

    @staticmethod
    @allure.step('Регистрация юзера')
    def user_registration(email=None, password=None, need_generate_data=True):
        response = requests.post(f'{data.BASE_URL}{data.REGISTER_URL}', data={
    "email": email,
    "password": password
})
        if need_generate_data:
            data_user = generate_data_for_registration()
            response = requests.post(f'{data.BASE_URL}{data.REGISTER_URL}', data=data_user)
        return response.status_code, response.json()