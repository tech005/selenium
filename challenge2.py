from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# starting the browser and going to python
driver = webdriver.Firefox()
driver.get("http://wiki.python.org/moin/FrontPage")

# find the search element
searchbox = driver.find_element_by_id('searchinput')
# searchbox = driver.find_element_by_xpath("//*[@id="searchinput"]")

# clear the entry
searchbox.clear()

# send keys to fill 
searchbox.send_keys("Beginner")
searchbox.send_keys(Keys.RETURN)
time.sleep(5)

# find select box and change by visible text
selectbox = Select(driver.find_element_by_xpath("//*/form/div/select"))
selectbox.select_by_visible_text("Raw Text")
time.sleep(5)
driver.close()