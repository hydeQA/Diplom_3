from pages.personal_account_page import Personal_Account_Page
from locators.personal_account_page_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
import allure
import burger_api
from urls import Urls

class TestPersonalAccountPage:
    @allure.title("Проверка успешного открытия личного кабинета авторизованного пользователя")
    @allure.description("Проверка перехода в 'Личный кабинет' кликом по кнопке 'Личный кабинет' на главной странице")
    def test_open_personal_account_success(self, driver):
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        account_page = Personal_Account_Page(driver)
        account_page.open()
        email = account_page.get_user_email(user_data)
        password = account_page.get_user_password(user_data)
        account_page.click_account_button()
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        account_page.wait_and_find_element(PersonalAccountLocators.TITLE_MAIN_PAGE)
        account_page.click_account_button()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert account_page.is_element_present(PersonalAccountLocators.DESCRIPTION_ACCOUNT)

    @allure.title("Проверка успешного перехода в раздел 'История заказов'")
    @allure.description("Проверка успешного перехода в раздел 'История заказов' в личном кабинете "
                        "авторизованного пользователя")
    def test_redirect_to_order_history_page_success(self, driver):
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        account_page = Personal_Account_Page(driver)
        account_page.open()
        email = account_page.get_user_email(user_data)
        password = account_page.get_user_password(user_data)
        account_page.click_account_button()
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        account_page.wait_and_find_element(PersonalAccountLocators.TITLE_MAIN_PAGE)
        account_page.click_account_button()

        account_page.click_order_history_btn()

        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert driver.current_url == (Urls.BASE_URL + Urls.ORDER_HISTORY_URL)

    @allure.title("Проверка успешного выхода из аккаунта")
    @allure.description("Проверка успешного выход из аккаунта кликом по кнопке 'Выход' в 'Личном Кабинете'")
    def test_exit_account_success(self, driver):
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        account_page = Personal_Account_Page(driver)
        account_page.open()
        email = account_page.get_user_email(user_data)
        password = account_page.get_user_password(user_data)
        account_page.click_account_button()
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        account_page.wait_and_find_element(PersonalAccountLocators.TITLE_MAIN_PAGE)
        account_page.click_account_button()

        account_page.click_exit_btn()
        account_page.wait_and_find_element(PersonalAccountLocators.TITLE_LOGIN_PAGE)

        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert driver.current_url == (Urls.BASE_URL + Urls.LOGIN_URL)