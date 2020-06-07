from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "/basket" in self.browser.current_url, "Current URL is not basket URL"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET, timeout=2)

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in message