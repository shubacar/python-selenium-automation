from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART = (By.ID, 'add-to-cart-button')


@when("Click on the cart button")
def click_cart(context):
     context.driver.find_element (*ADD_TO_CART).click()

