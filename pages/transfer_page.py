from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TransferPage(BasePage):

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")

    AMOUNT_INPUT = (By.ID, "amount")

    FROM_ACCOUNT = (By.ID, "fromAccountId")

    TO_ACCOUNT = (By.ID, "toAccountId")

    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1")


    def go_to_transfer_page(self):

        self.click(self.TRANSFER_LINK)


    def transfer_money(self, amount):

        self.type(self.AMOUNT_INPUT, amount)

        self.click(self.TRANSFER_BUTTON)


    def get_success_text(self):

        return self.get_text(self.SUCCESS_MESSAGE)