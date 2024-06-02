from pages.base_page import BasePage
from urls import Urls
from locators.recovery_password_page_locators import RecoveryPassPageLocators
from locators.personal_account_page_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
import allure

class Personal_Account_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в шапке страницы")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.driver.execute_script("arguments[0].click();",
                                   account_button)  # Клик через JavaScript, потому что в Firefox кнопка перекрывается модальным окном
    @allure.step("Получить Email для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получить Password для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Ввести почту в поле email")
    def set_email(self, email):
        input_email = self.wait_and_find_element(PersonalAccountLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Ввести пароль в поле 'Пароль'")
    def set_password(self, password):
        input_password = self.wait_and_find_element(PersonalAccountLocators.FIELD_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Авторизоваться кликом по кнопке 'Войти'")
    def click_enter_button(self):
        enter_button = self.wait_and_find_element(PersonalAccountLocators.ENTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", enter_button)