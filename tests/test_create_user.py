import requests
import pytest
import allure
from random_user import RandomUser
from responses import Responses
from urls import Urls


@allure.description("Создание уникального пользователя")
def test_create_unique_user(create_and_delete_user):
    user = RandomUser()
    user_data = {"email": user.email, "password": user.password, "name": user.name}

    register_response = requests.post(Urls.url_register, data=user_data)
    assert register_response.status_code == 200
    assert register_response.json() == {'success': True, 'user': {'email': user.email, 'name': user.name},
                                        'accessToken': register_response.json().get('accessToken'), 'refreshToken':
                                            register_response.json().get('refreshToken')}


@allure.description("Создание пользователя, который уже зарегистрирован")
def test_create_existing_user():
    user = RandomUser()
    user_data = {
        "email": user.email,
        "password": user.password,
        "name": user.name
    }
    requests.post(Urls.url_register, data=user_data)
    register_response = requests.post(Urls.url_register, data=user_data)
    assert register_response.status_code == 403
    assert register_response.json() == Responses.create_existing_user


@allure.description("Создание пользователя с незаполненным одним из обязательных полей")
@pytest.mark.parametrize("user_data", [{"email": "", "password": "password", "name": "Username"},
                                       {"email": "test-data@yandex.ru", "": "password", "name": "Username"},
                                       {"email": "test-data@yandex.ru", "password": "password", "name": ""}
                                       ])
def test_create_user_without_all_fields(user_data):
    response = requests.post(Urls.url_register, data=user_data)

    assert response.status_code == 403
    assert response.json() == Responses.create_user_without_all_fields
