import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'https://www.linkedin.com/jobs/search/?geoId=102264497&keywords=python&location=Ukraine'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
driver.get(url)

sign_in_button = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
sign_in_button.click()
email_form = driver.find_element(By.ID, 'username')
email_form.send_keys('your email')
password_form = driver.find_element(By.ID, 'password')
password_form.send_keys('your password')
sign_in_button = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
sign_in_button.click()
save_job_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
save_job_button.click()
