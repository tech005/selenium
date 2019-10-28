import pathlib
from selenium import webdriver

# get current working dir for reference
current_dir = pathlib.Path(__file__).parent


# create instance of firefox and call it
driver = webdriver.Firefox()

# getting the html from a file
driver.get("file:///"+str(current_dir)+"/form.html")

# get element by id from html
login_form = driver.find_element_by_id("loginForm")

# output to screen
print("My login form element is:")
print(login_form)

# close the browser
driver.close()