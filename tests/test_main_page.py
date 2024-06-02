from pages.main_page import Main_Page
from locators.main_page_locators import MainPageLocators
import allure
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

    @allure.title("Проверка успешного открытия всплывающего окна с информацией об Ингридиенте")
    @allure.description("Проверка открытия всплывающего окна с информацией об Ингридиенте после клика по Ингридиенту")
    def test_open_ingredient_card_success(self, driver):
        main_page = Main_Page(driver)
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.is_element_present(MainPageLocators.INGREDIENT_TITLE)

    @allure.title("Проверка успешного закрытия всплывающего окна с информацией об Ингридиенте")
    @allure.description("Проверка закрытия всплывающего окна с информацией об Ингридиенте после клика по кнопке 'Крестик'")
    def test_close_ingredient_card_success(self, driver):
        main_page = Main_Page(driver)
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert main_page.is_element_present(MainPageLocators.TITLE_MAIN_PAGE)






'''
Проверка основного функционала
всплывающее окно закрывается кликом по крестику
1. Открыть страницу Стеллар Бургер
2. Кликнуть по "Ингредиенту"
3. Закрыть всплывающее окно на крестик
4. Проверить что отбражается "Соберите бургер"
'''