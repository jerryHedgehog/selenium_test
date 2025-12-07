from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@Given("Open page")
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.maximize_window()


@When("Fill first name")
def fill_first_name(context):
    context.driver.find_element(By.ID, "firstName").send_keys("John")

@When("Fill last name")
def fill_last_name(context):
    context.driver.find_element(By.ID, "lastName").send_keys("Doe")

@When("Select gender")
def select_gender(context):
    context.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()

@When("Fill phone number")
def fill_phone_number(context):
    context.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

@When("Scroll to submit button")
def scroll_to_submit_button(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@When("Submit form")
def submit_form(context):
    context.driver.find_element(By.ID, "submit").click()

@Then("Success modal appeared")
def assert_success_modal_title(context):
    success_modal_title = context.driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    assert success_modal_title == "Thanks for submitting the form"