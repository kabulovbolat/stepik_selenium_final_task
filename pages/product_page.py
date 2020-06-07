from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def check_for_message_product_is_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME).text
        assert product_name == added_product_name, "Added item isn't equal product: {} != {} with URL: {}"\
            .format(product_name, added_product_name, self.browser.current_url)

    def check_for_correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_BASKET_PRICE).text
        assert product_price == basket_total_price, "Wrong basket price when added item: {} != {}"\
            .format(product_price, basket_total_price)

    def check_adding_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), \
            "Product adding message must be absent"

    # def check_adding_message_is_disappeared(self):
    #     assert self.is_disappeared(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), \
    #         "Product adding message must be disappeared"

    def should_be_success_message(self):
        message = "success message is not presented, but should be"
        assert self._is_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=1), message

    def should_not_be_success_message(self):
        message = "success message is presented, but should not be"
        assert self._is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=1), message

    def success_message_should_disappear(self):
        message = "success message still present, but should disappear"
        assert self._is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), message