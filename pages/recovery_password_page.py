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
