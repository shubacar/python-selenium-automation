from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_COUNT=(By.ID, 'nav-cart-count')

#@when("The cart opens")
#def cart_opens(context):


@then("Verify the cart has {expected_count} item")
def cart_count(context,expected_count):
     context.driver.implicitly_wait(4)
     actual_count=context.driver.find_element(*CART_COUNT).text
     print(actual_count)
     assert expected_count == actual_count , f'Expected result {expected_count}, got actual result{actual_count}'