import helpers

BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/api'
REGISTER_URL = '/signup'
CREATE_AD_URL = '/create-listing'
LOGIN_URL = '/signin'
UPDATE_AD_URL = '/update-offer'
DELETE_AD_URL = '/listings'

EMAIL = 'testakulava@loli.ru'
PASSWORD = 'qwerty123'
MESSAGE_FOR_NOT_UNIQUE_USER = 'Почта уже используется'
MESSAGE_FOR_UPDATE_NOT_MINE_AD = 'Оффер не найден или у вас нет прав на его редактирование'
MESSAGE_FOR_SUCCESS_DELETE_AD = 'Объявление удалено успешно'
ID_NOT_MINE_AD = 800

DATA_FOR_CREATE_AD = {
    "price": "0",
    "name": f"{helpers.generate_random_string(10)}",
    "category": "Авто",
    "condition": "Новый",
    "city": "Москва",
    "description": "Test description"
}

UPDATE_DATA_FOR_AD = {
    "price": "10",
    "name": f"{helpers.generate_random_string(10)}",
    "category": "Авто",
    "condition": "Новый",
    "city": "Москва",
    "description": "Test description"
}