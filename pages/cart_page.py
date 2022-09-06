from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    AMAZON_CART_EMPTY_TEXT=(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")

    def  verify_cart_content(self):
        expected_result = 'Your Amazon Cart is empty'
        print(expected_result)
        actual_result = self.find_element(*self.AMAZON_CART_EMPTY_TEXT).text
        assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
        print('Amazon cart empty test passed')