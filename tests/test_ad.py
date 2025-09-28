import allure
import data
from methods.ad_methods import AdMethods


class TestAd:

    @allure.title('Проверка создания объявления')
    def test_create_ad(self, create_ad):
        assert create_ad[0] == 201 and create_ad[1]['name'] == data.DATA_FOR_CREATE_AD['name']

    @allure.title('Проверка редактирования объявления')
    def test_update_ad(self, login_user, create_ad):
        update_ad = AdMethods.update_ad(login_user[1]['token']['access_token'], create_ad[1]['id'])
        assert update_ad[0] == 200 and update_ad[1]['name'] == data.UPDATE_DATA_FOR_AD['name']

    @allure.title('Проверка редактирования чужого объявления')
    def test_update_not_mine_ad(self, login_user):
        update_ad = AdMethods.update_ad(login_user[1]['token']['access_token'], data.ID_NOT_MINE_AD)
        assert update_ad[0] == 401 and update_ad[1]['message'] == data.MESSAGE_FOR_UPDATE_NOT_MINE_AD

    @allure.title('Проверка удаления объявления')
    def test_delete_ad(self, login_user, create_ad):
        delete_ad = AdMethods.delete_ad(login_user[1]['token']['access_token'], create_ad[1]['id'])
        assert delete_ad[0] == 200 and delete_ad[1]['message'] == data.MESSAGE_FOR_SUCCESS_DELETE_AD