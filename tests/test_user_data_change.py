import allure
import requests

from responses import Responses
from urls import Urls


@allure.description("Изменение данных пользователя с авторизацией")
def test_auth_user_change_data(auth_user):
    user_email_updated = {"email": 'oo12psoo12ps@yandex.ru'}
    headers = {'Authorization': auth_user["access_token"]}

    update_email_response = requests.patch(Urls.url_user, data=user_email_updated, headers=headers)

    assert update_email_response.status_code == 200
    assert update_email_response.json() == {
        "success": True,
        "user": {"email": user_email_updated['email'], "name": auth_user['name']}
    }

    user_name_updated = {"name": 'Yulia'}
    update_name_response = requests.patch(Urls.url_user, data=user_name_updated, headers=headers)

    assert update_name_response.status_code == 200
    assert update_name_response.json() == {
        "success": True,
        "user": {"email": user_email_updated['email'], "name": user_name_updated['name']}
    }
    delete_user_response = requests.delete(Urls.url_user, headers=headers)


@allure.description("Изменение данных пользователя без авторизации")
def test_unauth_user_change_data():
    response = requests.patch(Urls.url_user)
    assert response.status_code == 401
    assert response.json() == Responses.unauth_user
