import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = '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'
url = 'https://www.python.org/'
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
events_menu = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')
events = {}

for i, event in enumerate(events_menu):
    event_list = event.text.split('\n')
    events[i] = {'time': event_list[0], 'name': event_list[1]}

print(events)

driver.quit()
