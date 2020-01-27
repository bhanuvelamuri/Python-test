from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="/bhanu/geckodriver")
driver.maximize_window()
driver.get('http://makemytrip.com')
driver.find_element_by_xpath("//*[@id='fromCity']").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")
fromcities = driver.find_elements_by_css_selector("p[class*='blackText']")
for fromcity in fromcities:
    if fromcity.text in "Delhi, India":
        fromcity.click()
driver.find_element_by_xpath("//input[@placeholder='To']").send_keys("Deline")
driver.find_element_by_xpath("//p[@text='Deline, Canada']").click()