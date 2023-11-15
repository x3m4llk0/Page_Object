# describes objects and methods applicable on login page

from .base_page import BasePage
from .locators import LoginPageLocators
import time
from faker import Faker
f = Faker()

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "accounts/login/" in self.url, "This is not the login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The registration form is missing"

    def register_new_user(self):
        email = f.email()
        password = f.password()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PW1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PW2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
        self.should_be_authorized_user()
        print(email)
        print(password)


