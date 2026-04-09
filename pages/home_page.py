from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://parabank.parasoft.com/parabank/index.htm"

    USERNAME_INPUT = (By.NAME, "username")

    PASSWORD_INPUT = (By.NAME, "password")

    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")


    def open(self):

        super().open(self.URL)


    def login(self, username, password):

        self.type(self.USERNAME_INPUT, username)

        self.type(self.PASSWORD_INPUT, password)

        self.click(self.LOGIN_BUTTON)