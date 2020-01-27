from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="/bhanu/geckodriver")
driver.maximize_window()
driver.get('http://exciteservices.net')
print(driver.current_url)
print(driver.title)
driver.get('https://www.rahulshettyacademy.com/angularpractice/')
driver.find_element_by_name("name").send_keys("bhanu")
driver.find_element_by_name("email").send_keys("bhanu@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Bprpqwe")
dropdown = Select(driver.find_element_by_xpath("//*[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(0)
driver.find_element_by_xpath("//*[@value='Submit']").click()
message = driver.find_element_by_class_name("alert").text
assert "Success" in message
driver.close()