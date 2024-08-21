import pytest
import requests

from random_user import RandomUser
from urls import Urls


@pytest.fixture
def create_and_delete_user():
    user = RandomUser()
    user_data = {"email": user.email, "password": user.password, "name": user.name}

    # Создание пользователя
    requests.post(Urls.url_register, data=user_data)

    # Авторизация пользователя
    login_response = requests.post(Urls.url_login, data=user_data)
    access_token = login_response.json().get('accessToken')

    # Возвращаем словарь с токеном (без "Bearer ") и именем пользователя
    yield {"access_token": access_token, "name": user.name}

    # Удаление пользователя
    requests.delete(Urls.url_user, headers={'Authorization': f'Bearer {access_token}'})

@pytest.fixture
def auth_user(create_and_delete_user):
    # Возвращаем access_token, который будет использоваться в тестах
    return create_and_delete_user
