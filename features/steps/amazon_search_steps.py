from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FOOTER_LINKS= (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td a')
#BESTSELLER_LINKS=(By.CSS_SELECTOR, 'div#CardInstanceHJfhe_6apsjfPZA8gX_eDQ div ul li')
BESTSELLER_LINKS=(By.CSS_SELECTOR, "div[id*='CardInstance'] div ul li a")
BESTSELLER_BUTTON=(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
SEARCH_BUTTON=(By.ID, 'nav-search-submit-button')

@given("Open Amazon page")
def open_amazon(context):
     #context.driver.get('https://www.amazon.com/')
     context.app.main_page.open_main()



@when("Search for {search_product}")
def search_product(context,search_product):
    #DOMcontext.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_product)
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    #DOMcontext.driver.wait = WebDriverWait(context.driver, 10)
    #DOMcontext.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON), message='Search button not found').click()
#page object implementation
    context.app.header.search_product(search_product)

@when("Click on bestsellers")
def click_bestsellers(context):
    #context.driver.find_element(*BESTSELLER_BUTTON).click()
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(EC.element_to_be_clickable(BESTSELLER_BUTTON),message='Best seller not clickable').click()


@then("Verify {expected_link_count} bestsellers are shown")
def list_bestsellers(context,expected_link_count):
    best_seller_links=context.driver.find_elements(*BESTSELLER_LINKS)
    print (len(best_seller_links))
    expected_link_count=int(expected_link_count)
    print(expected_link_count)
    assert len(best_seller_links) == expected_link_count, f'Expected result {expected_link_count}, got actual result {len(best_seller_links)}'


@then("Verify {expected_result} are shown")
def verify_search(context,expected_result):
    #expected_result = '"mugs"'
    #actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #assert expected_result==actual_result, f'Expected result {expected_result}, got actual result{actual_result}'
    context.app.search_results_page.verify_search_results(expected_result)


#@then("Click on the add to cart button")
#def add_cart(context):
 #   context.driver.find_element(*ADD_TO_CART).click()

@then("Whether {expected_amt} footer links are shown")
def verify_footer_links(context,expected_amt):
    links=context.driver.find_elements(*FOOTER_LINKS)
    expected_amt=int(expected_amt)
    print(links)
    print(type(links))
    assert len(links)==expected_amt, f'Expected result {expected_amt}, got actual result {len(links)}'
