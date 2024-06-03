from selenium.webdriver.common.by import By

class OrderListPageLocators:
    ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[2]")
    INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")