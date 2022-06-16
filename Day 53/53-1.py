import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager


os.environ['GH_TOKEN'] = ''  # your gh-token


class RentalFinder:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.links = []
        self.prices = []
        self.addresses = []

    def __del__(self):
        self.driver.quit()

    def find_rentals(self):
        url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22user' \
              'sSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.3038' \
              '9632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%2' \
              '2%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3A' \
              'false%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%' \
              '3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afa' \
              'lse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B' \
              '%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%' \
              '22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
        self.driver.get(url)
        scrollable_elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '.photo-cards > li'))
        )

        for element in scrollable_elements:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        all_rentals = soup.findAll(name='div', class_='list-card-info')

        for rental in all_rentals:
            link = rental.find_next(name='a')['href'].replace('/b/', 'https://www.zillow.com/homedetails/')
            self.links.append(link)
            price = rental.find_next(name='div', class_='list-card-price').text[:6]
            self.prices.append(price)
            address = rental.find_next(name='address', class_='list-card-addr').text
            self.addresses.append(address)

    def fill_form(self):
        for rental in range(len(self.addresses)):
            url = ''  # your google form link
            self.driver.get(url)
            address_form = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby=\'i1\'')
            address_form.send_keys(self.addresses[rental])
            price_form = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby=\'i5\'')
            price_form.send_keys(self.prices[rental])
            link_form = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby=\'i9\'')
            link_form.send_keys(self.links[rental])
            send_button = self.driver.find_element(By.CSS_SELECTOR, 'span[class=\'NPEfkd RveJvd snByac\'')
            send_button.click()
            time.sleep(1)


bot = RentalFinder()
bot.find_rentals()
bot.fill_form()
