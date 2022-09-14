import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_incorrect_login(self):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Create driver
        driver = webdriver.Chrome("/Users/deniskondratuk/PycharmProjects/QaComplexAppG5/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("User11")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("Psw11")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_empty_login(self):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/deniskondratuk/PycharmProjects/QaComplexAppG5/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open page")

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_register(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Create driver
        driver = webdriver.Chrome("/Users/deniskondratuk/PycharmProjects/QaComplexAppG5/chromedriver")

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open page")

        # Fill username
        user = self.random_str()
        username_value = f"{user}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{user}{self.random_num()}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click on Sign Up button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("User was registered")
        sleep(1)

        # Verify register success
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        self.log.info("Registration for user '%s' was success and verified", username_value)
