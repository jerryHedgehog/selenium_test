from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_object.practice_form_page import PracticeFormPage

@Given("Open page")
def open_page(context):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.open_page()

@When("Fill first name {first_name}")
def fill_first_name(context, first_name):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.fill_first_name(first_name)


@When("Fill last name {last_name}")
def fill_last_name(context, last_name):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.fill_last_name(last_name)

@When("Select gender")
def select_gender(context):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.select_gender_male()

@When("Fill phone number")
def fill_phone_number(context):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.fill_phone_number("1234567890")

@When("Scroll to submit button")
def scroll_to_submit_button(context):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.scroll_to_submit_button()

@When("Submit form")
def submit_form(context):
    practice_form_page = PracticeFormPage(context.browser)
    practice_form_page.submit_form()

@Then("Assert success modal title")
def assert_success_modal_title(context):
    practice_form_page = PracticeFormPage(context.browser)
    success_modal_title = practice_form_page.expected_success_modal_title()
    assert success_modal_title == "Thanks for submitting the form"