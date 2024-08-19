import requests

from random_user import RandomUser
import allure

from responses import Responses
from urls import Urls


@allure.description("Получение заказов авторизованного пользователя")
def test_get_auth_user_orders():
    user = RandomUser()
    user_data = {"email": user.email, "password": user.password, "name": user.name}

    register_response = requests.post(Urls.url_register, data=user_data)

    login_response = requests.post(Urls.url_login, data=user_data)
    print(login_response.json())

    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    create_order_response = requests.post(Urls.url_orders, data=order_data)
    print(create_order_response.json())

    orders_response = requests.get(Urls.url_orders,
                                   headers={'Authorization': login_response.json().get('accessToken')})

    print(orders_response.status_code)
    print(orders_response.json())
    assert orders_response.json().get('success') is True

    delete_response = requests.delete(Urls.url_user,
                                      headers={'Authorization': register_response.json().get('accessToken')})
    assert delete_response.status_code == 202
    assert delete_response.json() == Responses.user_deleted_success


@allure.description("Получение заказов неавторизованного пользователя")
def test_get_unauth_user_orders():
    response = requests.get(Urls.url_orders)
    assert response.json() == Responses.unauth_user
