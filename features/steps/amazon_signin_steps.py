from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')
ORDER_BUTTON=(By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]")

@given("User opens the logged out Amazon page")
def open_amazon(context):
     context.driver.get('https://www.amazon.com/')


@when("User clicks on the orders")
def click_order(context):
    #context.driver.find_element(By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]").click()
    #POM
    context.app.header.click_orders()

@when("User clicks on the button on sign in popup")
def click_signin_popup(context):
    context.driver.wait.until (EC.element_to_be_clickable(SIGN_IN_POPUP_BTN),message='No sign in popup found').click()

@then("Verify signin is clickable")
def verify_signin_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='No sign in popup found')


@when("Wait for {sec} seconds")
def wait_8_seconds(context,sec):
    print(sec)
    sleep(int(sec))


@then("Verify signin disappears")
def signin_disappear(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN), message='Sign in popup still found')

@then("Sign in page opens")
def verify_signin(context):
    expected_result = "Sign-In"
    context.app.signin_page.verify_signin_page()
        #print(expected_result)
        #actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text
        #assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
        #context.driver.find_element(By.ID, 'ap_email')
        #print('First Amazon HW case passed')

