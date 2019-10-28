import pathlib
from selenium import webdriver

# get current working dir for reference
current_dir = pathlib.Path(__file__).parent


# create instance of firefox
driver = webdriver.Firefox()

# getting the html from a file
driver.get("file:///"+str(current_dir)+"/form.html")

# get element by id from html
content = driver.find_element_by_class_name("content")

# output to screen
print("My class element is:")
print(content)

# close the browser
driver.close()