from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span a.btn-default[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PW1_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PW2_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD2CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages strong")
    ADD2CART_PRICE = (By.CSS_SELECTOR, "div.alertinner>p strong")

class BasketPageLocators():
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items h3 a")