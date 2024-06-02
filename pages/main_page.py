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
        ingredients_list = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.INGREDIENT_LIST))
        ingredients = ingredients_list.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.driver.execute_script("arguments[0].click();", second_ingredient)

    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(MainPageLocators.X_BUTTON)
        self.driver.execute_script("arguments[0].click();", x_button)


