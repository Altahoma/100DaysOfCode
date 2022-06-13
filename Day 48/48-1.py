import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'https://rozetka.com.ua/ua/pro_service_18303670/p281479973/'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
price = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'product-prices__big'))
)
print(price.text)

driver.quit()
