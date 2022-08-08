from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_COLLECTION=(By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR=(By.CSS_SELECTOR,"#variation_color_name .selection")

@given("User opens specific {expected_product} page")
def open_product_page(context,expected_product):
    context.driver.get(f'https://www.amazon.com/dp/{expected_product}')

@then("User can find colors")
def find_colors(context):
    expected_colors=['Purple','Black','Blue','Malachite Green','Red','White']
    colors=context.driver.find_elements(*COLOR_COLLECTION)
    actual_colors=[]
    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]

    print(actual_colors)


    assert expected_colors==actual_colors, f' expected colors {expected_colors}, got {actual_colors}'