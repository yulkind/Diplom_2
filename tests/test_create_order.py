import allure
from api_client import ApiClient
from responses import Responses
from urls import Urls

# Создаём экземпляр ApiClient с базовым URL
api_client = ApiClient(Urls.url_orders)


@allure.description("Создание заказа с авторизацией")
def test_auth_user_create_order(create_and_delete_user):
    response = api_client.create_order(
        ingredients=["61c0c5a71d1f82001bdaaa6d"],
        auth_token=create_and_delete_user["access_token"]
    )
    assert response.status_code == 200


@allure.description("Создание заказа без авторизации")
def test_unauth_user_create_order():
    response = api_client.create_order(
        ingredients=["61c0c5a71d1f82001bdaaa6d"]
    )
    assert response.status_code == 200


@allure.description("Создание заказа с ингредиентами")
def test_create_order_with_ingredients():
    response = api_client.create_order(
        ingredients=["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    )
    assert response.status_code == 200


@allure.description("Создание заказа без ингредиентов")
def test_create_order_without_ingredients():
    response = api_client.create_order(ingredients=[])
    assert response.status_code == 400
    assert response.json() == Responses.create_order_without_ingredients


@allure.description("Создание заказа с неверным хешем ингредиентов")
def test_create_order_with_incorrect_hash():
    response = api_client.create_order(ingredients=["0d3b41a"])
    assert response.status_code == 500
