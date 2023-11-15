import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # reads the language param from the CLI
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")


@pytest.fixture(scope="function")  # starts the browser in the defined language.
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\033[38;5;63m\nstart browser for test..\033[0;0m \033[38;5;39m \nlanguage:{user_language} \033[0;0m")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser...")
    browser.quit()