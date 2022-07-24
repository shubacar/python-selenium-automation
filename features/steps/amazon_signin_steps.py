from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("User opens the logged out Amazon page")
def open_amazon(context):
     context.driver.get('https://www.amazon.com/')


@when("User clicks on the cart")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]").click()

@then("Sign in page opens")
def verify_signin(context):
    expected_result = "Sign-In"
    print(expected_result)
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text
    assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
    context.driver.find_element(By.ID, 'ap_email')
    print('First Amazon HW case passed')

