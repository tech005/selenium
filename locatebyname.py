import pathlib
from selenium import webdriver

# get current working dir for reference
current_dir = pathlib.Path(__file__).parent


# create instance of firefox and call it
driver = webdriver.Firefox()

# getting the html from a file
driver.get("file:///"+str(current_dir)+"/form.html")

# get element by id from html
username = driver.find_element_by_name('username')
# output to screen
print("My input element is:")
print(username)

# close the browser
driver.close()