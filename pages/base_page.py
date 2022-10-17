import allure
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    @allure.step
    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        return self.waiter.until(
            method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)),
            message=f"XPATH: '{xpath}' is not displayed or cannot be found",
        )

    @allure.step
    def wait_until_clickable(self, xpath):
        """Wait until element is clickable"""
        return self.waiter.until(
            method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)),
            message=f"XPATH: '{xpath}' is not clickable or cannot be found",
        )

    @allure.step
    def is_exists(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    @allure.step
    def fill_field(self, xpath, value):
        """Find, Clear and fill field"""
        element = self.wait_until_clickable(xpath=xpath)
        element.clear()
        element.send_keys(value)

    @allure.step
    def click(self, xpath):
        """Find and click"""
        self.wait_until_clickable(xpath=xpath).click()

    @allure.step
    def get_element_text(self, xpath):
        """Find element and get text"""
        element = self.wait_until_displayed(xpath=xpath)
        return element.text
