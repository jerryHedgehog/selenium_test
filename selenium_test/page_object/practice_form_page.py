from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PracticeFormPage:
    PAGE_URL = "https://demoqa.com/automation-practice-form"
    SELECTORS = {
        "first_name": (By.ID, "firstName"),
        "last_name": (By.ID, "lastName"),
        "gender_male": (By.CSS_SELECTOR, "label[for='gender-radio-1']"),
        "phone_number": (By.ID, "userNumber"),
        "submit_button": (By.ID, "submit"),
        "success_modal_title": (By.CLASS_NAME, "modal-title"),
        "success_modal_phone_number": (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
    }

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def open_page(self):
        self.driver.get(self.PAGE_URL)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PracticeFormPage:
    PAGE_URL = "https://demoqa.com/automation-practice-form"
    SELECTORS = {
        "first_name": (By.ID, "firstName"),
        "last_name": (By.ID, "lastName"),
        "gender": (By.CSS_SELECTOR, "label[for='gender-radio-1']"),
        "phone_number": (By.ID, "userNumber"),
        "submit_button": (By.ID, "submit"),
        "success_modal_title": (By.CLASS_NAME, "modal-title"),
        "success_modal_phone_number": (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
    }

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.SELECTORS['first_name']).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.SELECTORS['last_name']).send_keys(last_name)

    def select_gender_male(self):
        element = self.driver.find_element(*self.SELECTORS['gender_{gender}'])
        self.driver.execute_script("arguments[0].click();", element)

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.SELECTORS['phone_number']).send_keys(phone_number)

    def submit_form(self):
        element = self.driver.find_element(*self.SELECTORS['submit_button'])
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_submit_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.SELECTORS['submit_button']))

    def expected_success_modal_title(self):
        return self.driver.find_element(*self.SELECTORS['success_modal_title']).text