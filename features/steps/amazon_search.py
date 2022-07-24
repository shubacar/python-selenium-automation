from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("Open Amazon page")
def open_amazon(context):
     context.driver.get('https://www.amazon.com/')


@when("Search for Mugs")
def search_mugs(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('mugs')


@then("Verify mugs are shown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify mugs are shown')