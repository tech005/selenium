# implicit waits pause for a certain time for every action
# waiting is timed in seconds
from selenium import webdriver

driver= webdriver.Firefox()

driver.implicitly_wait(10)

driver.get('http://www.python.org')
myDynamicElement = driver.find_element_by_id('start-shell')

driver.close()