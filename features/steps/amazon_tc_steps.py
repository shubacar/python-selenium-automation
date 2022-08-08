from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.XPATH, "//a[contains(@href, 'amazon.com/privacy')]")
PRIVACY_NOTICE_TEXT = (By.XPATH, "//h1[contains(text(),'Amazon.com Privacy Notice')]")

@given("User open Amazon T&C page")
def open_amazon(context):
     context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when("Store original windows")
def store_original_windows(context):
     context.driver.original_window=context.driver.current_window_handle


@when("Click on Amazon Privacy Notice link")
def click_privacy_link(context):
     context.driver.wait.until(EC.element_to_be_clickable(PRIVACY_LINK), message='No privacy link found').click()


@when("Switch to the newly opened window")
def switch_privacy_link(context):
     context.driver.wait.until(EC.new_window_is_opened)
     new_window=context.driver.window_handles[1]
     context.driver.switch_to.window(new_window)


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_page(context):
     expected_result = 'Amazon.com Privacy Notice'
     actual_result = context.driver.find_element(*PRIVACY_NOTICE_TEXT ).text
     assert expected_result == actual_result, f'Expected result {expected_result}, got actual result{actual_result}'


@then("User can close new window and switch back to original")
def switch_back(context):
     context.driver.close()
     context.driver.switch_to.window(context.driver.original_window)