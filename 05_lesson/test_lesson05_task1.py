from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.org/")

        start_url = driver.current_url

        html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        html_form_link.click()

        assert driver.current_url.endswith("/forms/post")

        driver.back()

        assert driver.current_url == start_url

    finally:
        driver.quit()
