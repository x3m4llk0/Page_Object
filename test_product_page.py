"""
pytest -v --tb=line --language=en -m need_review test_product_page.py
"""
import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"




class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.click_add2cart_button()
        page.should_be_add2cart_msg()
        page.should_be_add2cart_price()


@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6',
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  '8', '9'])   #parametrization adds numbers to the link

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, number):
    link_param = f'{link}?promo=offer{number}'
    page = ProductPage(browser, link_param) # init PageObject, pass an instance of driver and link_param to the constr
    page.open()                         # opens the page
    page.click_add2cart_button()        # adds to cart
    page.solve_quiz_and_get_code()      # calculates the formula and inputs the answer
    page.should_be_add2cart_msg()       # checks the message is present
    page.should_be_add2cart_price()     # checks the price is correct

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add2cart_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add2cart_button()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasePage(browser, link)
    page.open()        
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_cart_is_empty()   # cart should be empty
    basket_page.should_be_text_cart_is_empty()    # text cart is empty exists