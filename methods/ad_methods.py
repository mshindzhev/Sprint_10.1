import allure
import requests

import data


class AdMethods:

    @staticmethod
    @allure.step('Создание объявления')
    def edit_user(token, new_data):
        response = requests.patch(f'{data.BASE_URL}/auth{data.USER_URL}', headers={'Authorization': token}, json=new_data)
        return response.status_code, response.json()

