import pytest
import allure
from allure_commons.types import AttachmentType
from page_object.practice_form_page import PracticeFormPage
from test_data.test_data_demoqa_form import TestDataDemoQAForm

@allure.feature("DemoQA Form")
class TestDemoQaForm:
    # To jest ok, o ile zmieniłeś plik test_data na zmienne statyczne (bez __init__)
    Test_Data = TestDataDemoQAForm()

    # ---------------- TEST 1 ----------------
    @allure.story("Fill form with valid data")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Submit form with valid data")
    def test_submit_form_with_valid_data(self, driver, practice_form_page):
        # Act
        with allure.step("open page"):
            practice_form_page.open_page()
        with allure.step("fill first name"):
            # Używamy TestDataDemoQAForm (bez self, bo to klasa statyczna)
            practice_form_page.fill_first_name(TestDataDemoQAForm.first_name)
        with allure.step("fill last name"):
            practice_form_page.fill_last_name(TestDataDemoQAForm.last_name)
        with allure.step("select gender"):
            practice_form_page.select_gender_male()
        with allure.step("fill phone number"):
            practice_form_page.fill_phone_number(TestDataDemoQAForm.phone_number)
        with allure.step("fill subject"):
            practice_form_page.fill_subject(TestDataDemoQAForm.subject)
        with allure.step("scroll to submit button"):
            practice_form_page.scroll_to_submit_button()
        with allure.step("submit form"):
            practice_form_page.submit_form()

        # Assert
        with allure.step("assert success modal title"):
            assert practice_form_page.expected_success_modal_title() == "Thanks for submitting the form"

        with allure.step("attach screenshot"):
            # POPRAWKA: Używamy 'driver', a nie 'remote_chrome_driver'
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


    # ---------------- TEST 2 ----------------
    @allure.story("Fill form with invalid data")
    @allure.severity(allure.severity_level.NORMAL)
    # POPRAWKA: Zmieniamy argument z 'remote_chrome_driver' na 'driver'
    def test_submit_form_with_invalid_data(self, driver, practice_form_page):
        # Act
        with allure.step("open page"):
            practice_form_page.open_page()
        with allure.step("fill first name"):
            practice_form_page.fill_first_name("Artur22")
        with allure.step("fill last name"):
            practice_form_page.fill_last_name("Kowalski22")
        with allure.step("select gender"):
            practice_form_page.select_gender_male()
        with allure.step("fill phone number"):
            practice_form_page.fill_phone_number("1234567890")
        with allure.step("scroll to submit button"):
            practice_form_page.scroll_to_submit_button()
        with allure.step("submit form"):
            practice_form_page.submit_form()

        # Assert
        with allure.step("assert success modal title"):
            assert practice_form_page.expected_success_modal_title() == "Thanks for submitting the form"

        with allure.step("attach screenshot"):
            # POPRAWKA: Tutaj też 'driver'
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)