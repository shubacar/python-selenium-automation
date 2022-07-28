from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON=(By.CSS_SELECTOR, "div#nav-cart-count-container")

@when("User clicks on the cart icon")
def click_cart(context):
     context.driver.find_element(*CART_ICON).click()

#@then("Verifies that the cart is empty")
#def verify_cart_click(context):
    #expected_result = 'Your Amazon Cart is empty'
    #print(expected_result)
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    #assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
    #print('Amazon cart empty test passed')

