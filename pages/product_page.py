from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def click_add2cart_button(self):  # Add2cart method
        self.browser.find_element(*ProductPageLocators.ADD2CART_BTN).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_add2cart_msg(self):  # Check Add2cart message
        product_name_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is missing"
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), "Add to cart message is missing"
        assert product_name_msg == product_added_msg, f"PRODUCT NAME='{product_name_msg}' MESSAGE ='{product_added_msg}'"

    def should_be_add2cart_price(self):  # Check Add2cart price
        sale_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add2cart_price = self.browser.find_element(*ProductPageLocators.ADD2CART_PRICE).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is missing"
        assert self.is_element_present(*ProductPageLocators.ADD2CART_PRICE), "Add to cart price is missing"
        assert sale_price == add2cart_price, f"Sale price is '{sale_price}', while Add to cart price is '{add2cart_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MSG), "Success message is present, but should not be"

