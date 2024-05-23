from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import csv
import subprocess
import login_fb_with_cookies as login

browser = login.browser
subprocess.call(['python', 'login_fb_with_cookies.py'])

facebook_post_url = "https://www.facebook.com/groups/onlyfifaonline/posts/814403573954813/"

browser.get(facebook_post_url)
time.sleep(1)
browser.execute_script("window.scrollTo(0, window.scrollY + 1100);")
time.sleep(random.randint(1,3))

button = browser.find_element(By.XPATH, '//*[@class="xt0b8zv x2bj2ny xrbpyxo xl423tq"]')
button.click()
time.sleep(random.randint(3,5))


images = browser.find_elements(By.XPATH, '//*[@class="xb57i2i x1q594ok x5lxg6s x78zum5 xdt5ytf x6ikm8r x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1odjw0f x1e4zzel x1tbbn4q x1y1aw1k x4uap5 xwib8y2 xkhd6sd"]')
a = images.find_elements(By.XPATH, '//*[@class="x78zum5 xdt5ytf x1iyjqo2 x1n2onr6"')
last_height = browser.execute_script("return arguments[0].scrollHeight;", a)
time.sleep(random.randint(4,5))




# path = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\react.csv"
# with open(path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["user","type"])

browser.close()

