import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_order(self, ingredients, auth_token=None):
        # Создаём headers как пустой словарь, а если есть токен, добавляем его
        headers = {}
        if auth_token:
            headers['Authorization'] = auth_token
        order_data = {"ingredients": ingredients}
        return requests.post(self.base_url, json=order_data, headers=headers)

