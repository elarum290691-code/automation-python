from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )

    DELAY = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay = self.wait.until(
            EC.visibility_of_element_located(self.DELAY)
        )
        delay.clear()
        delay.send_keys(str(value))

    def click_button(self, value):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{value}']")
            )
        )
        button.click()

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.SCREEN,
                "15"
            )
        )
        return self.driver.find_element(*self.SCREEN).text
