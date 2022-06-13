import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'http://orteil.dashnet.org/experiments/cookie/'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
cookie = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 60 * 5
time_to_buy = time.time() + 5

while True:
    cookie.click()

    if time.time() > time_to_buy:
        time_to_buy += 5
        money = int(driver.find_element(By.ID, 'money').text)
        store_items = driver.find_elements(By.CSS_SELECTOR, '#store b')
        upgrades = {}

        for item in store_items[:8]:
            name, price = item.text.replace(',', '').replace(' ', '').split('-')
            upgrades[name] = int(price)

        affordable_upgrade = ''
        for name, price in upgrades.items():
            if money > price:
                affordable_upgrade = name

        if affordable_upgrade:
            upgrade = driver.find_element(By.ID, f'buy{affordable_upgrade}')
            upgrade.click()
            print(f'Bought {affordable_upgrade}')

    if time.time() > timeout:
        cookie_per_second = driver.find_element(By.ID, 'cps').text
        print(cookie_per_second)
        break
