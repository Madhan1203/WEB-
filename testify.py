import selenium
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.quantumapalooza.com/")

print(driver.find_element_by_xpath("/html/body").text)
driver.close()

