from selenium.webdriver.common.by import By

class OrderListPageLocators:
    ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[2]")
    INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    CLOSE_WINDOW_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    ORDER_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    ORDER_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")

