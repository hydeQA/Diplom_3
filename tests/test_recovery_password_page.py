from pages.recovery_password_page import Recovery_Password_Page
from locators.recovery_password_page_locators import RecoveryPassPageLocators
import allure

class TestRecoveryPassPage:

    @allure.title('Проверка успешного перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description("Проверка успешного перехода с главной страницы в личный кабинет и далее на страницу "
                        "восстановления пароля, кликом по кнопке 'Восстановить пароль'")
    def test_success_recovery_pass(self, driver):
        recovery_page = Recovery_Password_Page(driver)
        recovery_page.open()
        recovery_page.click_account_button()
        recovery_page.click_recovery_button()
        assert recovery_page.is_element_present(RecoveryPassPageLocators.RECOVER_TITLE)