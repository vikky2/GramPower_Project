from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
driver.execute_script("window.scrollTo(0, 300)")

Email_add=driver.find_element_by_id("email").send_keys("vikky.ranjan2@gmail.com")

Password=driver.find_element_by_id("passwd").send_keys("vikky123")

SignIn=driver.find_element_by_id("SubmitLogin").click()

