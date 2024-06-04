from pages.order_list_page import OrderListPage
from locators.order_list_page_locators import OrderListPageLocators
import allure
import burger_api

class TestOrderListPage:
    @allure.title("Проверка успешного открытия окна с деталями заказа на 'Ленте треков'")
    @allure.description("Проверка успешного перехода по кнопке 'Конструктор' в шапке сайта")
    def test_open_detail_order_window_success(self, driver):
        order_list_page = OrderListPage(driver)
        order_list_page.open()
        order_list_page.click_list_order_button()
        order_list_page.click_order_card()
        assert order_list_page.is_element_present(OrderListPageLocators.INGREDIENT_IN_ORDER)

    @allure.title("Проверка появления номера нового заказа на экране 'Лента заказов'")
    @allure.description("Создаём заказ и проверяем, что его номер появляется среди всех заказова на странице 'Лента заказов'")
    def test_order_in_order_list_success(self, driver):
        # Создаём и авторизуем нового пользователя
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        order_list_page = OrderListPage(driver)
        order_list_page.open()
        email = order_list_page.get_user_email(user_data)
        password = order_list_page.get_user_password(user_data)
        order_list_page.click_account_button()
        order_list_page.set_email(email)
        order_list_page.set_password(password)
        order_list_page.click_enter_button()
        order_list_page.wait_and_find_element(OrderListPageLocators.TITLE_MAIN_PAGE)
        # Создаём заказ бургера с булкой моусом и мясом
        order_list_page.add_bun_in_order()
        order_list_page.add_sauce_in_order()
        order_list_page.add_meat_in_order()
        order_list_page.click_create_order_button()
        order_list_page.click_order_card_x_button()
        # Переходим на экран "История заказов" и получаем номер последнего заказа
        order_list_page.wait_and_find_element(OrderListPageLocators.TITLE_MAIN_PAGE)
        order_list_page.click_account_button()
        order_list_page.click_order_history_btn()
        order_number = order_list_page.get_order_number()
        # Переходим на экран "Лента заказов" и получаем номер последнего заказа
        order_list_page.click_list_order_button()
        order_number_in_list = order_list_page.get_order_number()
        # Удаляем созданного пользователя
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert order_number == order_number_in_list

    @allure.title("Проверка увеличения значения счётчика заказов на экране 'Лента заказов'")
    @allure.description(
        "Создаём заказ и проверяем что счётчик всех заказов на экране 'Лента заказов' увеличивается на 1")
    def test_order_counter_increases_when_new_order_is_placed_success(self, driver):
        # Создаём и авторизуем нового пользователя
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        order_list_page = OrderListPage(driver)
        order_list_page.open()
        email = order_list_page.get_user_email(user_data)
        password = order_list_page.get_user_password(user_data)
        order_list_page.click_account_button()
        order_list_page.set_email(email)
        order_list_page.set_password(password)
        order_list_page.click_enter_button()
        order_list_page.wait_and_find_element(OrderListPageLocators.TITLE_MAIN_PAGE)
        # Получаем значение счётчика заказов на странице "Лента заказов"
        order_list_page.click_list_order_button()
        counter_before = order_list_page.get_orders_counter()
        # Переходим в конструктор и создаём заказ
        order_list_page.click_constructor_button()
        order_list_page.add_bun_in_order()
        order_list_page.add_sauce_in_order()
        order_list_page.add_meat_in_order()
        order_list_page.click_create_order_button()
        order_list_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем значение счётчика всех заказов
        order_list_page.click_list_order_button()
        counter_after = order_list_page.get_orders_counter()
        # Удаляем созданного пользователя
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert (counter_after - counter_before) == 1

'''
Раздел "Лента Заказов"
при создании нового заказа счётчик Выполнено за всё время увеличивается,
The order counter increases when a new order is placed
1. Создать пользователя и авторизоваться
2. Открыть страницу
3. Авторизоваться
4. Перейти на ленту заказов
5. Получить количество заказов
6. Перейти на Конструктор
7. Содзать бургер
4. Оформить заказ
5. Закрыть вплывающее окно
6. Перейти в Ленту заказов
7. Получить количество заказов
8. Проверить что разница между количествами заказов == 1
'''