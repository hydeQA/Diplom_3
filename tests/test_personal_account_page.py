import time

from pages.personal_account_page import Personal_Account_Page
from locators.recovery_password_page_locators import RecoveryPassPageLocators
from locators.personal_account_page_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from data import UserData
import allure
import burger_api

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
        account_page.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE)
        account_page.click_account_button()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert account_page.is_element_present(PersonalAccountLocators.DESCRIPTION_ACCOUNT)




        '''
        Личный кабинет
        Переход по клику на "Личный кабинет"
        1. V Создать тело для регистрации пользователя генератором даных V
        2. V Зарегистрировать пользователя с этими данными
        3. V Получить Email из сгенерированных данных
        4. V Получить Password из сгенерированных данных
        5. V Открыть главную страницу
        6. V Кликнуть кнопку "Личный кабинет"
        5. В поле Email ввести почту из сгенерированных данных
        5. В поле Пароль ввести пароль из сгенерированных данных
        7. Кликнуть кнопку Войти
        8. Кликнуть на кнопку "Личный кабинет"
        9. Проверить что на странице есть текст "В этом разделе вы можете изменить свои персональные данные"
        '''