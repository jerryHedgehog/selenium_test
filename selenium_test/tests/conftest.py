import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def remote_chrome_driver():
    # The URL of your Hub
    HUB_URL = "http://localhost:4444"

    # 1. Define the desired browser/platform (The Node's capability)
    chrome_capabilities = DesiredCapabilities.CHROME.copy()

    # 2. Connect to the Hub using RemoteWebDriver
    driver = webdriver.Remote(
        command_executor=f'{HUB_URL}',  # /wd/hub',
        options=webdriver.ChromeOptions()  # Use 'options' for modern Selenium 4
    )
    # Note: For Selenium 3, you would pass desired_capabilities directly.
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def remote_firefox_driver():
    # The URL of your Hub
    HUB_URL = "http://localhost:4444"

    # 1. Define the desired browser/platform (The Node's capability)
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()

    # 2. Connect to the Hub using RemoteWebDriver
    driver = webdriver.Remote(
        command_executor=f'{HUB_URL}',  # /wd/hub',
        options=webdriver.FirefoxOptions()  # Use 'options' for modern Selenium 4
    )
    # Note: For Selenium 3, you would pass desired_capabilities directly.
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def remote_edge_driver():
    # The URL of your Hub
    HUB_URL = "http://localhost:4444"

    # 1. Define the desired browser/platform (The Node's capability)
    edge_capabilities = DesiredCapabilities.EDGE.copy()

    # 2. Connect to the Hub using RemoteWebDriver
    driver = webdriver.Remote(
        command_executor=f'{HUB_URL}',  # /wd/hub',
        options=webdriver.EdgeOptions()  # Use 'options' for modern Selenium 4
    )
    # Note: For Selenium 3, you would pass desired_capabilities directly.
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def practice_form_page(driver):
    from page_object.practice_form_page import PracticeFormPage
    return PracticeFormPage(driver)