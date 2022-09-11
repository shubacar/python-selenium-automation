from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDER_BUTTON = (By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]")
    CART_ICON = (By.CSS_SELECTOR, "div#nav-cart-count-container")
    FLAG= (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    LANGUAGE = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPT_SELECT= (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS=(By.XPATH, "//span[contains(text(),'New Arrivals')]")
    NEW_BOYS=(By.XPATH, "//h3[text()='Boys']")

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

    def hover_lang(self):
        flag=self.find_element(*self.FLAG)
        actions=ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_language(self):
        self.wait_for_element_appear(*self.LANGUAGE)

    def hover_newarrivals(self):
        newarrivals=self.find_element(*self.NEW_ARRIVALS)
        actions=ActionChains(self.driver)
        actions.move_to_element(newarrivals)
        actions.perform()

    def verify_newarrivals(self):
        self.wait_for_element_appear(*self.NEW_BOYS)


    def select_dept(self,alias):
        department=self.find_element(*self.DEPT_SELECT)
        select = Select(department)
        select.select_by_value(f'search-alias={alias}')