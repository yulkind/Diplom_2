## Дипломный проект. Задание 2: API
### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы тесты API, покрывающие сценарии создания пользователя, логина пользователя, изменение данных пользователя, создание заказа, получение заказов конкретного пользователя.     

Сделан Allure-отчёт (отчёт: http://192.168.100.10:55737/index.html)

### Структура проекта
- `tests` - папка, содержащая тесты, разделённые по эндпоинтам. Например, создание пользователя, логин пользователя и т.д.

### Запуск автотестов

**Установка зависимостей**

> `pip install -r requirements.txt`/ `py -m pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчёта**

>  `pytest --alluredir=allure_results`/ `py -m pytest --alluredir=allure_results`
>  `allure serve allure_results`
