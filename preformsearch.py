from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# starting the browser and going to python
driver = webdriver.Firefox()
driver.get("http://python.org")

# find the search element
search = driver.find_element_by_name('q')

# clear the entry
search.clear()

# send keys to fill 
search.send_keys("pycon")

# hit return to submit
search.send_keys(Keys.RETURN)

# display results for 4 seconds then close the browser
time.sleep(4)
driver.close()
