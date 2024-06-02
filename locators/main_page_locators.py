from selenium.webdriver.common.by import By

class MainPageLocators:

    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
