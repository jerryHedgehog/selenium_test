# Testy Automatyczne (Python + Selenium + Allure + Behave)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0-green)
![Behave](https://img.shields.io/badge/Behave-BDD-orange)
![Pytest](https://img.shields.io/badge/Test_Runner-Pytest-yellow)
![Allure](https://img.shields.io/badge/Report-Allure-9cf)
![Grid](https://img.shields.io/badge/Infrastructure-Selenium_Grid-cac)

> *Pliki z zajęć kursu CodeBrainers z zakresu testów automatycznych*

## Technologie
W projekcie wykorzystano następujący stos technologiczny:

* **Język programowania:** Python 3.14
* **Biblioteka webowa:** Selenium WebDriver (wersja 4.38)
* **Test Runner:** Pytest
* **BDD Framework:** Behave (styl Cucumbera)
* **Wzorce projektowe:** Page Object Model (POM)
* **Raportowanie:** Allure Framework
* **Infrastruktura:** Selenium Grid (RemoteWebDriver)
* **Przeglądarki:** Chrome, Edge

## Spis treści
* [O projekcie](#o-projekcie)
* [Struktura projektu](#struktura-projektu)
* [Technologie](#technologie)
* [Jak uruchomić testy](#jak-uruchomić-testy)
* [Scenariusze testowe](#scenariusze-testowe)

## O projekcie
Kod znajdujący się w tym repozytorium został stworzony w ramach ćwiczeń praktycznych podczas kursu **CodeBrainers** (16.10.2025 - 04.12.2025).

Projekt obejmuje automatyzację testów formularza na stronie **DemoQA** i demonstruje dwie ścieżki testowe:
1. **Klasyczne testy Pytest** - czyste podejście programistyczne.
2. **Testy BDD (Behave)** - scenariusze pisane językiem naturalnym (Gherkin), zrozumiałe dla biznesu.

Zastosowano tu wzorzec projektowy **Page Object Model (POM)**, aby oddzielić logikę testów od struktury strony, co zapewnia czytelność i łatwiejsze utrzymanie kodu.

## Struktura projektu
```text
selenium_test/
├── features/               # Testy BDD (Gherkin)
│   ├── steps/              # Implementacja kroków (Python)
│   │   └── environment.py  # Konfiguracja środowiska (Hooks)
│   └── *.feature           # Scenariusze testowe
├── page_object/            # Mapy elementów (Page Object Model)
├── tests/                  # Testy klasyczne (Pytest)
└── test_data/              # Dane testowe

## Scenariusze testowe

1. Poprawne wypełnienie formularza (Happy Path)
Wypełnienie wszystkich pól obowiązkowych (Imię, Nazwisko, Płeć, Telefon).
Weryfikacja pojawienia się modala z potwierdzeniem ("Thanks for submitting the form").
2. Walidacja danych (Data Driven Testing)
Testy parametryzowane (Scenario Outline) sprawdzające formularz dla różnych zestawów danych osobowych (różne imiona i nazwiska).
3. Testy na różnych przeglądarkach
Weryfikacja działania na Chrome oraz Edge przy użyciu RemoteWebDriver.
