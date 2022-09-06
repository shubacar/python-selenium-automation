from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self,expected_result):
        actual_result = self.driver.find_element(*self.RESULT).text
        assert expected_result == actual_result, f'Expected result {expected_result}, got actual result{actual_result}'
