from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
Sign_up=driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
Sign_up.click()

driver.execute_script("window.scrollTo(0, 300)")

E_mail=driver.find_element_by_id("email_create")
E_mail.send_keys("vikky.ranjan2@gmail.com")
Create_Account=driver.find_element_by_xpath("//button[@id='SubmitCreate']")
Create_Account.click()

driver.execute_script("window.scrollTo(0, 50)")


title=driver.find_element_by_id("id_gender1")
title.click()

F_name=driver.find_element_by_name("customer_firstname")
F_name.send_keys("Vikky")

L_name=driver.find_element_by_name("customer_lastname")
L_name.send_keys("Ranjan")

Passwrd=driver.find_element_by_name("passwd")
Passwrd.send_keys("vikky123")

driver.execute_script("window.scrollTo(0, 400)")

Dob_date=driver.find_element_by_id("days")
days=Select(Dob_date)
days.select_by_value("31")

Dob_month=driver.find_element_by_id("months")
month=Select(Dob_month)
month.select_by_value("8")

Dob_year=driver.find_element_by_id("years")
year=Select(Dob_year)
year.select_by_value("1994")

company=driver.find_element_by_id("company").send_keys("Bizdom Technologies")

address1=driver.find_element_by_id("address1").send_keys("hsr layout sector-3")

address2=driver.find_element_by_id("address2").send_keys("sector-3")

city=driver.find_element_by_id("city").send_keys("Bengaluru")

state=driver.find_element_by_id("id_state")
stat=Select(state)
stat.select_by_value("6")

pincode=driver.find_element_by_name("postcode").send_keys("00000")

driver.execute_script("window.scrollTo(0, 300)")

mobile_phone=driver.find_element_by_id("phone_mobile").send_keys("8386973745")

address_alias=driver.find_element_by_id("alias").send_keys("MY Address")

register=driver.find_element_by_id("submitAccount").click()

#driver.close()