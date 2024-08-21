import requests

from random_user import RandomUser
import allure

from responses import Responses
from urls import Urls


@allure.description("Логин под существующим пользователем")
def test_user_login_successful():
    user = RandomUser()
    user_data = {
        "email": user.email,
        "password": user.password,
        "name": user.name
    }

    requests.post(Urls.url_register, data=user_data)

    login_response = requests.post(Urls.url_login, data=user_data)
    response_data = login_response.json()
    assert login_response.status_code == 200
    assert login_response.json() == {"success": True,
                                     "accessToken": response_data["accessToken"],
                                     "refreshToken": response_data["refreshToken"],
                                     "user": {
                                         "email": user.email,
                                         "name": user.name
                                     }
                                     }

    delete_response = requests.delete(Urls.url_user,
                                      headers={'Authorization': login_response.json().get('accessToken')})
    assert delete_response.status_code == 202
    assert delete_response.json() == Responses.user_deleted_success


@allure.description("Логин с неверным логином и паролем")
def test_user_login_with_incorrect_data():
    user = RandomUser()
    user_data = {"email": user.email, "password": user.password, "name": user.name}

    requests.post(Urls.url_login, data=user_data)

    login_response = requests.post(Urls.url_login, data=user_data)
    assert login_response.status_code == 401
    assert login_response.json() == Responses.user_login_with_incorrect_data

    requests.delete(Urls.url_user, headers={'Authorization': login_response.json().get('accessToken')})
