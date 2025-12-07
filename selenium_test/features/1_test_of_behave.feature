Feature: Test of Behave
    Scenario Outline: Fill form with valid data
        # AAA
        # Arrange
        Given Open page
        # Act
        When Fill first name <imie>
        And Fill last name <nazwisko>
        And Select gender
        And Fill phone number
        And Scroll to submit button
        And Submit form
        # Assert
        Then Success modal appeared

    Examples:
        | imie | nazwisko |
        | Artur | Kowalski |
        | Krzysztof | Nowak |
        | Jan | Kowalczyk |
        | Anna | Nowakowska |
        | Maria | Kowalczykowska |
        | Artur | Kowalski |
        | Krzysztof | Nowak |
        | Jan | Kowalczyk |
        | Anna | Nowakowska |
        | Maria | Kowalczykowska |