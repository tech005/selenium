from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# init the webdriver and get page
driver = webdriver.Firefox()
driver.get("http://www.nscc.ca")
time.sleep(2)

# find the searchbar
searchbar = driver.find_element_by_id("gsc-i-id1")

# clear searchbar
searchbar.clear()

# send keys
searchbar.send_keys("IT")
time.sleep(2)

# hit return
searchbar.send_keys(Keys.RETURN)
time.sleep(5)

# locate systems in results by xpath
systems = driver.find_element_by_xpath("/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/div[5]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/a")

# click it
systems.click()

time.sleep(10)

# close the window
driver.close()

