from selenium.webdriver.common.by import By
import random
import time
import csv
import subprocess
import login_fb_with_cookies as login

browser = login.browser
subprocess.call(['python', 'login_fb_with_cookies.py'])

facebook_post_url = "https://www.facebook.com/groups/onlyfifaonline/posts/814403573954813/"

browser.get(facebook_post_url)
time.sleep(random.randint(2,4))

browser.execute_script("window.scrollTo(0, window.scrollY + 1500);")
time.sleep(random.randint(1,3))

x, y = 0,0

def number_comments():
    global x, y
    text = browser.find_element(By.XPATH, '//*[@class="x6s0dn4 x78zum5"]')
    a = text.get_attribute('textContent')
    x, y = a.split('/')
    x = int(x)
    y = int(y)
    return x, y

show_also = browser.find_element(By.XPATH, '//*[@class="x78zum5 x1w0mnb xeuugli"]')


number_comments()
while y - x > 50:
    number_comments()
    show_also.click()
    browser.execute_script("window.scrollTo(0, window.scrollY + 1000);")
    time.sleep(2)
browser.execute_script("window.scrollTo(0,window.scrollY+ 1000)")
time.sleep(5)

a = browser.find_elements(By.XPATH,'//*[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"]')

b = browser.find_elements(By.XPATH, '//*[@class="x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')


# path1 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\comments.csv"
path = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\user.csv"


with open(path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['user'])
    for list in b:
        x = list.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        writer.writerow([x])

# with open(path1, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['comment'])
#     for list in a:
#         y = list.get_attribute('textContent').strip()
#         writer.writerow([y])




browser.close()
