Feature: Test of Behave

    Background: Common steps before each Scenario
        Given Open page

    Scenario: Fill form with valid data
        When Fill first name Artur
        And Fill last name Kowalski
        And Select gender
        And Fill phone number
        And Scroll to submit button
        And Submit form
        Then Assert success modal title

    Scenario Outline: Fill form with valid data
        When Fill first name <first_name>
        And Fill last name <last_name>
        And Select gender
        And Fill phone number
        And Scroll to submit button
        And Submit form
        Then Assert success modal title

        Examples:
            | first_name | last_name |
            | Artur      | Kowalski  |
            | Jan        | Kowalski  |
            | Anna       | Kowalski  |
            # | Maria      | Kowalski  |
            # | Tom        | Kowalski  |