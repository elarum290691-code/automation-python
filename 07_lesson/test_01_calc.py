from selenium import webdriver

from pages.calculator_page import CalculatorPage


def test_calc():
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)

        calculator.open()
        calculator.set_delay(45)

        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

        assert calculator.get_result() == "15"

    finally:
        driver.quit()
