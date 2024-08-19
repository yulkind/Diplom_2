import allure
import pytest
import requests

from random_user import RandomUser
#import allure

from responses import Responses
from urls import Urls


@allure.description("Изменение данных пользователя с авторизацией")
def test_auth_user_change_data():
    user = RandomUser()
    user_data = {"email": user.email, "password": user.password, "name": user.name}

    register_response = requests.post(Urls.url_register, data=user_data)

    requests.post(Urls.url_login, data=user_data)

    user_email_updated = {"email": 'oopsoops@yandex.ru'}
    update_email_response = requests.patch(Urls.url_user, data=user_email_updated,
                                           headers={'Authorization': register_response.json().get('accessToken')})
    assert update_email_response.status_code == 200
    assert update_email_response.json() == {"success": True,
                                            "user": {"email": user_email_updated['email'], "name": user.name}}

    user_name_updated = {"name": 'name'}
    update_name_response = requests.patch(Urls.url_user, data=user_name_updated,
                                          headers={'Authorization': register_response.json().get('accessToken')})
    assert update_name_response.status_code == 200
    assert update_name_response.json() == {"success": True, "user": {"email": user_email_updated['email'],
                                                                     "name": user_name_updated['name']}}

    delete_response = requests.delete(Urls.url_user, headers={'Authorization': register_response.json().get('accessToken')})
    assert delete_response.status_code == 202
    assert delete_response.json() == Responses.user_deleted_success


@allure.description("Изменение данных пользователя без авторизации")
def test_unauth_user_change_data():
    response = requests.patch(Urls.url_user)
    assert response.status_code == 401
    assert response.json() == Responses.unauth_user
