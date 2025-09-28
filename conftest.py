import pytest

import data
from methods.ad_methods import AdMethods
from methods.login_methods import LoginMethods
from methods.register_methods import RegisterMethods


@pytest.fixture
def create_user():
    create_user = RegisterMethods().user_registration(data.EMAIL, data.PASSWORD, True)
    return create_user

@pytest.fixture
def login_user():
    login_user = LoginMethods().user_login(data.EMAIL, data.PASSWORD)
    return login_user

@pytest.fixture
def create_ad(login_user):
    create_ad = AdMethods.create_ad(login_user[1]['token']['access_token'], data.DATA_FOR_CREATE_AD)
    return create_ad

