from pages.home_page import HomePage
from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By


class TestLogout:

    def test_logout_success(self, driver):

        home = HomePage(driver)

        home.open()


        # register new user
        register = RegisterPage(driver)

        register.go_to_register()

        register.register_user()


        # click logout
        driver.find_element(By.LINK_TEXT, "Log Out").click()


        # verify logout successful (login form visible)
        login_text = driver.find_element(By.XPATH, "//h2").text


        assert "Customer Login" in login_text