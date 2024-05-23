import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import time

chrome = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\.venv\chromedriver.exe"
facebook_url = "https://www.facebook.com"
service = Service(chrome)

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(random.randint(2,5))

browser.get(facebook_url)
phone= '0789138999'
password = 'dovancuong392004'

phone_input = browser.find_element(By.ID, 'email')
phone_input.send_keys(phone)

password_input = browser.find_element(By.ID, 'pass')
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)

time.sleep(random.randint(3,5))


cookies = browser.get_cookies()
path = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\cookies.pkl"
with open(path, "wb") as file:
    pickle.dump(cookies,file)