import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'https://en.wikipedia.org/wiki/Main_Page'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)


