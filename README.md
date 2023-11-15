# Educational Project: Page Object

This educational project demonstrates the usage of the Page Object pattern in automated testing. The project utilizes pytest and Selenium to create a test framework for a web application.

## Project Structure

- `conftest.py` - Contains pytest fixtures and configuration.
- `pytest.ini` - Configuration file for pytest.
- `requirements.txt` - Lists the required dependencies for the project.
- `test_main_page.py` - Contains test cases related to the main page of the web application.
- `test_product_page.py` - Contains test cases related to the product page of the web application.
- `pages/` - Directory containing the page object classes and locators.
  - `base_page.py` - Contains the base page class with common functionality shared by other page objects.
  - `basket_page.py` - Contains the page object class for the basket page.
  - `locators.py` - Contains the locators (selectors) used by the page objects.
  - `login_page.py` - Contains the page object class for the login page.
  - `main_page.py` - Contains the page object class for the main page.
  - `product_page.py` - Contains the page object class for the product page.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/x3m4llk0/Page_Object.git
2. Install the required dependencies. You can use pip to install the dependencies mentioned in the requirements.txt file:
    ```shell
    pip install -r requirements.txt
3. Set up the test environment. Make sure you have the necessary web drivers (e.g., ChromeDriver, GeckoDriver) installed and properly configured.

4. Run the tests. You can execute the test scripts using pytest:
    ```shell
    pytest
   
## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request.

