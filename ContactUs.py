from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://automationpractice.com/index.php?controller=contact") # Navigating to the url
driver.execute_script("window.scrollTo(0, 300)")

# Connectiung to the Contact us page
Subject_heading=driver.find_element_by_id("id_contact") # selecting the reason for contact
subject=Select(Subject_heading)
subject.select_by_value("2")

Message=driver.find_element_by_id("message").send_keys("Hi Team,")  # Providing additional details

Email_address=driver.find_element_by_id("email").send_keys("vikky.ranjan2@gmail.com")  # Entering email

order_reference=driver.find_element_by_id("id_order").send_keys("OR123")    # entreing password

Attach_file=driver.find_element_by_id("fileUpload").send_keys("C://Users//D//Desktop//note.txt")  #uploading a text file

Send=driver.find_element_by_id("submitMessage").click()   # clicking on Send button for response




