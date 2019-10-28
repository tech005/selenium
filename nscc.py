from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.nscc.ca")
time.sleep(3)

mynscc = driver.find_element_by_xpath("//*/header/div[1]/ul[1]/li[5]/a")
mynscc.click()
time.sleep(5)



driver.close()