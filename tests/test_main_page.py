from pages.main_page import Main_Page
import allure
import burger_api
from urls import Urls

class TestMainPage:
    @allure.title("Проверка успешного перехода по кнопке 'Конструктор'")
    @allure.description("Проверка успешного перехода по кнопке 'Конструктор' в шапке сайта")
    def test_open_main_page_clicK_constructor_btn_success(self, driver):
        main_page = Main_Page(driver)
        main_page.open()
        main_page.click_list_order_button()
        main_page.click_constructor_button()
        assert driver.current_url == Urls.BASE_URL

    @allure.title("Проверка успешного перехода по кнопке 'Лента заказов'")
    @allure.description("Проверка успешного перехода по кнопке 'Лента заказов' в шапке сайта")
    def test_open_list_order_page_success(self, driver):
        main_page = Main_Page(driver)
        main_page.open()
        main_page.click_list_order_button()
        assert driver.current_url == (Urls.BASE_URL + Urls.LIST_ORDER_PAGE)


'''
Проверка основного функционала
Проверка перехода на "Конструктор"
1. Открыть страницу Стеллар Бургер
2. Кликнуть по кнопке Лента заказов
3. Кликнуть по кнопке "Конструктор"
4. проверить что открылась главная страница
'''