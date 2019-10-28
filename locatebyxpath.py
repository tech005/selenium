import pathlib
from selenium import webdriver

# get current working dir for reference
current_dir = pathlib.Path(__file__).parent


# create instance of firefox and call it
driver = webdriver.Firefox()

# getting the html from a file
driver.get("file:///"+str(current_dir)+"/form.html")

# get element by id from html
login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form_relative = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")

# output to screen
print("My login form element is:")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)

# close the browser
driver.close()