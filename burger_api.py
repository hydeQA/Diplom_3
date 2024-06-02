import allure
import helper
from urls import Urls
import requests

@allure.step("Создать тело запроса создания юзера: email, password, name")
def create_user_body():
    return helper.new_user_login_password()

@allure.step("Создать пользователя в приложении Stellar burger")
def create_user(user_data):
    user_response = requests.post(Urls.API_URL+Urls.CREATE_USER_ENDPOINT, json=user_data)
    return user_response

@allure.step("Получить access token созданного пользователя")
def get_access_token(user_response):
    access_token = user_response.json().get("accessToken")
    return access_token

@allure.step("Удалить созданного пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    response_delete = requests.delete(Urls.BASE_URL + Urls.DELETE_USER_ENDPOINT, headers=headers)
    return response_delete

@allure.step("Авторизоваться в приложении Stellar burger")
def login_user(login_data):
    login_response = requests.post(Urls.BASE_URL + Urls.LOGIN_USER_ENDPOINT, json=login_data)
    return login_response

@allure.step("Изменить данные пользователя: email, password, name")
def change_user_data(access_token, new_data):
    headers = {"Authorization": access_token}
    change_data_response = requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT, headers=headers, json=new_data)
    return change_data_response

@allure.step("Получить refreshtoken созданного пользователя")
def get_refresh_token(user_response):
    refresh_token = user_response.json().get("refreshToken")
    return refresh_token

@allure.step("Получить список доступных ингредиентов")
def get_ingredients():
    response = requests.get(urls.BASE_URL + urls.GET_INGREDIENTS_ENDPOINT)
    return response

@allure.step("Создать заказ")
def create_new_order(headers, ingredients):
    response = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, headers=headers, json=ingredients)
    return response

@allure.step("Получить все заказы конкретного пользователя")
def get_users_orders(headers):
    response = requests.get(urls.BASE_URL + urls.GET_USER_ORDER, headers=headers)
    return response