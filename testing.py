from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://dayliffservice.freshworks.com/")
driver.maximize_window()

elem = driver.find_element_by_xpath("//*[@id='username']")
elem.send_keys("alex")
