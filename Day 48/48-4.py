import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'http://secure-retreat-92358.herokuapp.com/'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Homa')
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Eve')
email = driver.find_element(By.NAME, 'email')
email.send_keys('homa.eve.1@gmail.com')
sign_up = driver.find_element(By.CSS_SELECTOR, 'form button')
sign_up.click()

driver.quit()
