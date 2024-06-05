from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Main_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Лента заказов' в шапке страницы")
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BTN)
        self.driver.execute_script("arguments[0].click();", list_order_button)

    @allure.step("Кликнуть по кнопке 'Конструктор' в шапке страницы")
    def click_constructor_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_BTN)
        self.driver.execute_script("arguments[0].click();", list_order_button)

    @allure.step("Кликнуть по 'Ингредиенту' в 'Конструкторе'")
    def click_ingredient_button(self):
        ingredients_list = self.wait_and_find_element(MainPageLocators.INGREDIENT_LIST)
        ingredients = ingredients_list.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.driver.execute_script("arguments[0].click();", second_ingredient)

    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(MainPageLocators.X_BUTTON)
        self.driver.execute_script("arguments[0].click();", x_button)

    @allure.step("Перетащить булку в зону создания бургера")
    def add_bun_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить соус в зону создания бургера")
    def add_sauce_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.SAUCE_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить мясо в зону создания бургера")
    def add_meat_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.MEAT_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в шапке страницы")
    def click_create_order_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.driver.execute_script("arguments[0].click();", account_button)

    @allure.step("Получить количество ингредиентов из счётчика")
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(MainPageLocators.COUNTER)
        return counter_element.text

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
        input_email = self.wait_and_find_element(MainPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Ввести пароль в поле 'Пароль'")
    def set_password(self, password):
        input_password = self.wait_and_find_element(MainPageLocators.FIELD_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в шапке страницы")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", account_button)

    @allure.step("Авторизоваться кликом по кнопке 'Войти'")
    def click_enter_button(self):
        enter_button = self.wait_and_find_element(MainPageLocators.ENTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", enter_button)