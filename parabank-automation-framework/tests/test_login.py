from pages.home_page import HomePage
from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By


class TestLogin:

    def test_login_success(self, driver):

        home = HomePage(driver)

        home.open()

        register = RegisterPage(driver)

        register.go_to_register()

        username, password = register.register_user()

        # verify successful registration/login
        success_text = driver.find_element(By.TAG_NAME, "body").text

        assert "Welcome" in success_text