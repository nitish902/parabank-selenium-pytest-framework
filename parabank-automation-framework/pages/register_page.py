from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class RegisterPage(BasePage):

    # Locators
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    FIRST_NAME = (By.ID, "customer.firstName")

    LAST_NAME = (By.ID, "customer.lastName")

    ADDRESS = (By.ID, "customer.address.street")

    CITY = (By.ID, "customer.address.city")

    STATE = (By.ID, "customer.address.state")

    ZIP = (By.ID, "customer.address.zipCode")

    PHONE = (By.ID, "customer.phoneNumber")

    SSN = (By.ID, "customer.ssn")

    USERNAME = (By.ID, "customer.username")

    PASSWORD = (By.ID, "customer.password")

    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")

    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")


    # Actions
    def go_to_register(self):

        self.click(self.REGISTER_LINK)


    def register_user(self):

        # Dummy user data
        self.type(self.FIRST_NAME, "Test")

        self.type(self.LAST_NAME, "User")

        self.type(self.ADDRESS, "123 Test Street")

        self.type(self.CITY, "TestCity")

        self.type(self.STATE, "TS")

        self.type(self.ZIP, "12345")

        self.type(self.PHONE, "9999999999")

        self.type(self.SSN, "123456")


        # create unique username every time
        username = "testuser" + str(int(time.time()))

        password = "Password123"


        self.type(self.USERNAME, username)

        self.type(self.PASSWORD, password)

        self.type(self.CONFIRM_PASSWORD, password)

        self.click(self.REGISTER_BUTTON)


        # return credentials for login test
        return username, password