import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.firefox import GeckoDriverManager


USERNAME = ''  # your username
PASSWORD = ''  # your password
os.environ['GH_TOKEN'] = ''  # your gh-token


class InstaFollower:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.follow_list = []

    def login(self):
        url = 'https://www.instagram.com/accounts/login/'
        self.driver.get(url)

        username_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username'))
        )
        username_form.send_keys(USERNAME)
        password_form = self.driver.find_element(By.NAME, 'password')
        password_form.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'div.bkEs3:nth-child(3)')
        time.sleep(1)
        login_button.click()
        skip_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'button._a9--:nth-child(2)'))
        )
        skip_button.click()

    def find_followers(self):
        url = 'https://www.instagram.com/chefsteps/'
        self.driver.get(url)

        all_followers = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'li._aa_5:nth-child(2)'))
        )
        all_followers.click()
        scrollable_popup = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, '_aano'))
        )
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
        time.sleep(2)
        first_24_followers = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '._aae- li button'))
        )
        self.follow_list = first_24_followers

    def follow(self):
        for follower in self.follow_list:
            try:
                time.sleep(1)
                follower.click()
            except ElementClickInterceptedException:
                cansel_button = self.driver.find_element(By.CLASS_NAME, '_a9_1')
                cansel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
