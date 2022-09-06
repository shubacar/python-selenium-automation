from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDER_BUTTON = (By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]")
    CART_ICON = (By.CSS_SELECTOR, "div#nav-cart-count-container")

    #def search_product(self,search_product):
        #print(search_product)
        #self.input_text(self, search_product, *self.INPUT_FIELD)


    def click_cart(self):
        # context.driver.find_element(*CART_ICON).click()
        #self.wait.until(EC.element_to_be_clickable(*self.CART_ICON), message='No cart icon found').click()
        #self.wait_for_element_click(*self.CART_ICON).click()
        self.click(*self.CART_ICON)

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_orders(self):
        self.find_element(*self.ORDER_BUTTON).click()
        #self.click(*self.ORDER_BUTTON)