import random
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\.venv\chromedriver.exe"
facebook_url = "https://www.facebook.com"
service = Service(chrome)

options = Options()
options.add_argument("--disable-notifications")

browser = webdriver.Chrome(service=service, options=options)
browser.get(facebook_url)
time.sleep(random.randint(2,3))

path = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\cookies.pkl"

with open(path, "rb") as file:
    cookies = pickle.load(file)

for cookie in cookies:
    cookie['domain'] = '.facebook.com'
    try:
        browser.add_cookie(cookie)
    except Exception as e:
        print(e)




