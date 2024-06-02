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