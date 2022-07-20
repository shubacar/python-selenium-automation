#Find amazon logo by xpath
driver.find_element(By.xpath, "//i[@aria-label='Amazon']")

#Find continue button by id
driver.find_element(By.id,'Continue')

#Find need help link by xpath and using contains
driver.find_element(By.xpath, "//span[contains(text(),'Need help')]")
#Find Forgot your password link
driver.find_element(By.xpath, ("//a[contains(text(),'Forgot your password')]")

#Find Other issues with Sign-In link
driver.find_element(By.xpath, ("//a[@class='a-link-normal' and contains(text(),'Other')]")

#Find Register button
driver.find_element(By.xpath, ("//a[contains(@href, 'register')]")

#Find privacy link using multiple attributes

driver.find_element(By.xpath,("//div[@id='legalTextRow']//a[contains(@href, 'privacy')]")

