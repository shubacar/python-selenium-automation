from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    RESULT_DEPT=(By.CSS_SELECTOR, "#nav-subnav[data-category='{SUBSTRING}']")

    def get_subnav_locator(self,category):
        return [self.RESULT_DEPT[0],self.RESULT_DEPT[1].replace('{SUBSTRING}',category)]

    def verify_search_results(self,expected_result):
        actual_result = self.driver.find_element(*self.RESULT).text
        assert expected_result == actual_result, f'Expected result {expected_result}, got actual result{actual_result}'

    def verify_dept_selected(self,category):
        locator=self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)