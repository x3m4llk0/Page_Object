from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_cart_is_empty(self):               # check Cart has no items
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS), "Cart is not empty"

    def should_be_text_cart_is_empty(self):  # check text Cart is empty is present
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY), "Text Cart is empty is missing"