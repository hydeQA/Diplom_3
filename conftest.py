import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def chrome_driver():
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.get(Urls.BASE_URL)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(scope='function')
def firefox_driver():
    options = webdriver.FirefoxOptions()
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.maximize_window()
    firefox_driver.get(Urls.BASE_URL)
    yield firefox_driver
    firefox_driver.quit()