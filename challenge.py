from selenium import webdriver

site = "https://www.seleniumhq.org/"

# create instance of firefox
driver = webdriver.Firefox()

# getting the site
driver.get(site)

# get element by id 
element_id = driver.find_element_by_id("q")
print("element is")
print(element_id)

# get element by name
element_name = driver.find_element_by_name("q")
print("element is")
print(element_name)

# get by xpath
heading_xpath = driver.find_element_by_xpath("//*[@id='mainContent']/h2[1]")
print("element is")
print(heading_xpath)


# get by classname
element_classname = driver.find_elements_by_class_name("selineum-sponsors")
print("element is")
print(element_classname)


driver.close()
