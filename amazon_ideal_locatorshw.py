from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\careerauto\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.amazon.com/')


#find by class Amazon logo and create account label
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#find by id and css,id customer name and email
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

#find by multiple nodes for paassword tool tip
driver.find_element(By.XPATH, "//div[contains(text(), ' Passwords must be at least 6 characters.') and @class='a-alert-content']")

#find password an re-enter password
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
driver.find_element(By.ID, 'ap_password_check')

#find continue button
driver.find_element(By.CSS_SELECTOR, 'input#continue')

#find conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition']")

#find privacy link
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy']")

#find sign-in link
driver.find_element(By.CSS_SELECTOR, "a[href*='ap/signin?openid.pape.max_auth_age']")