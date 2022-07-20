from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\careerauto\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//span[@class='nav-line-2' and contains(text(),'Orders')]").click()


expected_result = "Sign-In"
print(expected_result)
actual_result = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text

print(actual_result)
assert expected_result == actual_result , f'Expected result {expected_result}, got actual result{actual_result}'
#find email input field

driver.find_element(By.ID, 'ap_email')
print('First Amazon HW case passed')

driver.quit()
