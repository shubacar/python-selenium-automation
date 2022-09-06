from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_PRICE= (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

#@given("Open Amazon page")
#def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


#@when("Search for {search_product}")
#def search_mugs(context,search_product):
  #  context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_product)
   # context.driver.find_element (By.ID, 'nav-search-submit-button').click()

#@then("Verify {expected_result} are shown")
#def verify_search(context,expected_result):
#    #expected_result = '"mugs"'
#    #print(expected_result)
#    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
#    #print(actual_result)
 #   assert expected_result == actual_result, f'Expected result {expected_result}, got actual result{actual_result}'


@when("Click on the first product")
def click_first_product(context):
    #context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE),
                              message='Best seller not clickable').click()


