import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    """Setup once before all features."""
    # Initialize WebDriver (Arrange)
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(3)
    context.browser.maximize_window()

    # Store the base URL for the context
    context.base_url = "https://demoqa.com/automation-practice-form"



def after_all(context):
    """Teardown once after all features."""
    # Quit the WebDriver (Cleanup)
    context.browser.quit()