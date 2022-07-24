from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\careerauto\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('mugs')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result='"mugs"'
print(expected_result)
actual_result=driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)
assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'

print('First Amazon test case passed')

driver.quit()