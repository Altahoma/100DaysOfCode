import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


PROMISED_DOWN = 100
PROMISED_UP = 50
EMAIL = ''  # your email
USERNAME = ''  # your username
PASSWORD = ''  # your password
os.environ['GH_TOKEN'] = ''  # your gh-token


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.ping = 0
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)
        start_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        start_button.click()
        time.sleep(60)
        self.ping = float(self.driver.find_element(By.CLASS_NAME, 'ping-speed').text)
        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        print(self.ping, self.down, self.up)

    def tweet_at_provider(self):
        url = 'https://twitter.com/i/flow/login'
        self.driver.get(url)

        email_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.r-30o5oe'))
        )
        email_form.send_keys(EMAIL)
        next_button = self.driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4:nth-child(6)')
        next_button.click()
        username_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.r-homxoj'))
        )
        username_form.send_keys(USERNAME)
        next_button = self.driver.find_element(By.CSS_SELECTOR, '.r-pw2am6')
        next_button.click()
        password_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.r-homxoj'))
        )
        password_form.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.r-19yznuf')
        login_button.click()
        text_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'notranslate'))
        )
        text_form.click()

        if self.down < 100 or self.up < 50:
            message = f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up ' \
                      f'when I pay for 100down/50up?'
        else:
            message = 'Today Internet connection is stable.'

        text_form.send_keys(message)
        text_form.send_keys(Keys.COMMAND + Keys.ENTER)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
