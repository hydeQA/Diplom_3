from pages.order_list_page import OrderListPage
from locators.order_list_page_locators import OrderListPageLocators
import allure

class TestOrderListPage:
    @allure.title("Проверка успешного открытия окна с деталями заказа на 'Ленте треков'")
    @allure.description("Проверка успешного перехода по кнопке 'Конструктор' в шапке сайта")
    def test_open_detail_order_window_success(self, driver):
        order_list_page = OrderListPage(driver)
        order_list_page.open()
        order_list_page.click_list_order_button()
        order_list_page.click_order_card()
        assert order_list_page.is_element_present(OrderListPageLocators.INGREDIENT_IN_ORDER)



'''
Раздел "Лента Заказов"
если кликнуть на заказ, откроется всплывающее окно с деталями

1. Открыть сайт стеллар бургер
2. Перейти на Ленту заказов
3. Кликнуть на заказ
4. Проверить что на всплыающем окне есть список с ингредиентами
'''