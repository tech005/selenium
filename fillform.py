import pathlib
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# get current working dir for reference
current_dir = pathlib.Path(__file__).parent

# create instance of firefox
driver = webdriver.Firefox()

# getting the html from a file
driver.get("file:///"+str(current_dir)+"/form2.html")

select= Select(driver.find_element_by_name('numReturnSelect'))
select.select_by_index(4)
time.sleep(2)
select.select_by_visible_text("500")
time.sleep(2)
select.select_by_value("800")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)
driver.close()