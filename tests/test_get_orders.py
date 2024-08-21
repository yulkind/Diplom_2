import requests
import allure
from responses import Responses
from urls import Urls


@allure.description("Получение заказов авторизованного пользователя")
def test_get_auth_user_orders(create_and_delete_user):
    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    requests.post(Urls.url_orders, data=order_data)

    orders_response = requests.get(Urls.url_orders,
                                   headers={'Authorization': create_and_delete_user['access_token']})
    assert orders_response.json().get('success') is True


@allure.description("Получение заказов неавторизованного пользователя")
def test_get_unauth_user_orders():
    response = requests.get(Urls.url_orders)
    assert response.json() == Responses.unauth_user
