from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListPageLocators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Лента заказов' в шапке страницы")
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BTN)
        self.driver.execute_script("arguments[0].click();", list_order_button)

    @allure.step("Открыть окно с деталями заказа кликом по карточке заказа")
    def click_order_card(self):
        order_card = self.wait_and_find_element(OrderListPageLocators.ORDER_CARD)
        self.driver.execute_script("arguments[0].click();", order_card)