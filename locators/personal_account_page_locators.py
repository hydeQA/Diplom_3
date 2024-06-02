from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    DESCRIPTION_ACCOUNT = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")