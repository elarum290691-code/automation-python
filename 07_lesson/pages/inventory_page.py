from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:

    BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    BOLT_TSHIRT = (
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )

    ONESIE = (
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    )

    CART = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    INVENTORY = (
        By.ID,
        "inventory_container"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY)
        )

    def add_backpack(self):
        self.driver.find_element(
            *self.BACKPACK
        ).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(
            *self.BOLT_TSHIRT
        ).click()

    def add_onesie(self):
        self.driver.find_element(
            *self.ONESIE
        ).click()

    def open_cart(self):
        self.driver.find_element(
            *self.CART
        ).click()
