import allure
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import data


class AdMethods:

    @staticmethod
    @allure.step('Создание объявления')
    def create_ad(token, data_dict):

        multipart_data = MultipartEncoder(fields=data_dict)

        response = requests.post(
            f'{data.BASE_URL}{data.CREATE_AD_URL}',
            headers={
                'Authorization': f'Bearer {token}',
                'Content-Type': multipart_data.content_type
            },
            data=multipart_data
        )
        return response.status_code, response.json(), multipart_data

    @staticmethod
    @allure.step('Обновление объявления')
    def update_ad(token, listing_id):
        response = requests.patch(f'{data.BASE_URL}{data.UPDATE_AD_URL}/{listing_id}', headers={
            "Authorization": f"Bearer {token}"
        }, data=data.UPDATE_DATA_FOR_AD)

        return response.status_code, response.json()

    @staticmethod
    @allure.step('Удаление объявления')
    def delete_ad(token, listing_id):
        response = requests.delete(f'{data.BASE_URL}/{data.DELETE_AD_URL}/{listing_id}', headers={
            "Authorization": f"Bearer {token}"
        })

        return response.status_code, response.json()
