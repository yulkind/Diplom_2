import requests
import allure

from random_user import RandomUser
from responses import Responses
from urls import Urls


@allure.description("Создание заказа с авторизацией")
def test_auth_user_create_order():
    user = RandomUser()
    user_data = {
        "email": user.email,
        "password": user.password,
        "name": user.name
    }
    requests.post(Urls.url_register, data=user_data)

    login_response = requests.post(Urls.url_login, data=user_data)

    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    create_order_response = requests.post(Urls.url_orders, data=order_data,
                                          headers={'Authorization': login_response.json().get('accessToken')})
    assert create_order_response.status_code == 200

    delete_response = requests.delete(Urls.url_user,
                                      headers={'Authorization': login_response.json().get('accessToken')})
    assert delete_response.status_code == 202
    assert delete_response.json() == Responses.user_deleted_success


@allure.description("Создание заказа без авторизации")
def test_unauth_user_create_order():
    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    response = requests.post(Urls.url_orders, data=order_data)
    assert response.status_code == 200


@allure.description("Создание заказа с ингредиентами")
def test_create_order_with_ingredients():
    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    response = requests.post(Urls.url_orders, data=order_data)
    assert response.status_code == 200


@allure.description("Создание заказа без ингредиентов")
def test_create_order_without_ingredients():
    order_data = {"ingredients": [""]}
    response = requests.post(Urls.url_orders, data=order_data)
    assert response.status_code == 400
    assert response.json() == Responses.create_order_without_ingredients


@allure.description("Создание заказа с неверным хешем ингредиентов")
def test_create_order_with_incorrect_hash():
    order_data = {"ingredients": ["0d3b41a"]}
    response = requests.post(Urls.url_orders, data=order_data)
    assert response.status_code == 500
