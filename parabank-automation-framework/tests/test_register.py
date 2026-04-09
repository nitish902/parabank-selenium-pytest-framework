from pages.home_page import HomePage
from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By


class TestRegister:

    def test_user_registration(self, driver):

        home = HomePage(driver)

        home.open()

        register = RegisterPage(driver)

        register.go_to_register()

        register.register_user()

        # verify success message
        success_message = driver.find_element(By.TAG_NAME, "h1").text

        assert "Welcome" in success_message