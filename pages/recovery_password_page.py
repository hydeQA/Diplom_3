from pages.base_page import BasePage
from urls import Urls
from locators.recovery_password_page_locators import RecoveryPassPageLocators
from locators.main_page_locators import MainPageLocators
import allure

class Recovery_Password_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в шапке страницы")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", account_button)  # Клик через JavaScript, потому что в Firefox кнопка перекрывается модальным окном

    @allure.step("Кликнуть по кнопке 'Восстановить пароль'")
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(RecoveryPassPageLocators.RECOVERY_BUTTON)
        self.driver.execute_script("arguments[0].click();", recovery_button)  # Клик через JavaScript, потому что в Firefox кнопка перекрывается модальным окном

    @allure.step("Ввести почту в поле email")
    def set_emil(self, email):
        input_email = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_button_recovery(self):
        recovery_button = self.wait_and_find_element(RecoveryPassPageLocators.BUTTON_RECOVERY)
        self.driver.execute_script("arguments[0].click();", recovery_button)

    @allure.step("Ввести новый пароль")
    def set_new_password(self, password):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_NEW_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Кликнуть по кнопке 'Глазик' отображения скрытого пароля")
    def click_show_password_button(self):
        eye_button = self.wait_and_find_element(RecoveryPassPageLocators.EYE_BUTTON)
        eye_button.click()

    @allure.step('Получить состояние поля пароля')
    def get_password_input_state(self):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_NEW_PASSWORD)
        return input_password.get_attribute("type") == "text"