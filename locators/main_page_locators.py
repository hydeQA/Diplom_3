from selenium.webdriver.common.by import By

class MainPageLocators:

    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    LIST_ORDER_BTN = (By.XPATH, "//p[text()='Лента Заказов']")
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
    INGREDIENT_BTN = (By.XPATH, ".//a[@class = '.BurgerIngredient_ingredient__1TVf6'] and text()='Краторная булка N-200i'")
    INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    INGREDIENT_LIST = (By.CLASS_NAME, "BurgerIngredients_ingredients__list__2A-mT")
    INGREDIENT_ITEM = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
    X_BUTTON = (By.XPATH, "//button[@type='button']")
    BURGER_ORDER = (By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[2]")
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[5]")
    MEAT_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[10]")

    CREATE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    CREATE_ORDER_DESCRIPTION = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")

    COUNTER_INGREDIENTS = (By.XPATH, "(//div[contains(@class, '.counter_default__28sqi')])[2]")
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[2]")

    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")