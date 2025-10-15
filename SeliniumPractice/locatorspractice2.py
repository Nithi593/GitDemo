import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(5)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmpassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#//button[text()='Save New Password']

time.sleep(5)







