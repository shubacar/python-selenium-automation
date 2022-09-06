from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):

    SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')
    #SIGN_IN_RES = (By.XPATH, "//h1[contains(text(),'Sign-In')]")

    SIGN_IN_RES = (By.XPATH, "//h1[@class='a-spacing-small']")
    SIGN_IN_EMAIL=(By.ID, 'ap_email')

    def click_signin_popup(self):
            #context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN),
                                      #message='No sign in popup found').click()
            self.find_element(* self.SIGN_IN_POPUP_BTN)
            self.click(* self.SIGN_IN_POPUP_BTN)


    def verify_signin_page(self):
        expected_result = 'Sign in'
        #self.verify_element_text(expected_result, *self.SIGN_IN_RES)
        actual_result = self.find_element(*self.SIGN_IN_RES).text
        print('actual result',actual_result)
        assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
        assert self.find_element(*self.SIGN_IN_EMAIL).is_displayed()
        # print('First Amazon HW case passed')
