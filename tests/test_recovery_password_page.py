from pages.recovery_password_page import Recovery_Password_Page
from locators.recovery_password_page_locators import RecoveryPassPageLocators
from data import UserData
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

    @allure.title("Проверка переход на экран 'Восстановление пароля' после ввода пароля и клика по кнопке "
                  "'Восстановить'")
    @allure.description("Проверка ввода почты и клика по кнопке 'Восстановить'")
    def test_input_email_and_click_button_success(self, driver):
        recovery_page = Recovery_Password_Page(driver)
        recovery_page.open()
        recovery_page.click_account_button()
        recovery_page.click_recovery_button()
        recovery_page.set_emil(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        assert recovery_page.is_element_present(RecoveryPassPageLocators.RECOVER_PASS_TITLE)

    @allure.title("Проверка работы кнопки раскрытия пароля 'Глазик' на экране восстановления пароля")
    @allure.description("На экране смены пароля кликаем на 'Глазик' для отображения скрытого пароля и проверяем"
                        " что поле становится активным")
    def test_eye_button_show_password_success(self, driver):
        recovery_page = Recovery_Password_Page(driver)
        recovery_page.open()
        recovery_page.click_account_button()
        recovery_page.click_recovery_button()
        recovery_page.set_emil(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()               # Нажать кнопку "Восстановить"
        recovery_page.set_new_password(UserData.NEW_PASSWORD)
        old_state = recovery_page.get_password_input_state()
        recovery_page.click_show_password_button()
        new_state = recovery_page.get_password_input_state()
        assert (old_state is False and new_state is True)
