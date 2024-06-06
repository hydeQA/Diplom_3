from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountLocators
import allure
from pages.recovery_password_page import RecoveryPasswordPage


class PersonalAccountPage(BasePage):
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
        self.click_element(enter_button)

    @allure.step("Кликнуть по кнопке 'История заказов' в Личном кабинете")
    def click_order_history_btn(self):
        order_history_btn = self.wait_and_find_element(PersonalAccountLocators.ORDER_HISTORY_BTN)
        self.click_element(order_history_btn)

    @allure.step("Кликнуть по кнопке 'Выход' в 'Личном Кабинете'")
    def click_exit_btn(self):
        exit_btn = self.wait_and_find_element(PersonalAccountLocators.EXIT_BTN)
        self.click_element(exit_btn)

    @allure.step("Получить номер последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(PersonalAccountLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Кликнуть по кнопке 'Восстановить пароль'")
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(PersonalAccountLocators.RECOVERY_BUTTON)
        self.click_element(recovery_button)
        return RecoveryPasswordPage(self.driver)