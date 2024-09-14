from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time
import random
import pyautogui



chrome_user_data_dir = r'C:\Users\ahmed\AppData\Local\Google\Chrome\User Data'
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")
chrome_options.add_argument(f"profile-directory=Default")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chromedriver_path = r'C:\\Program Files (x86)\\chromedriver.exe'
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.linkedin.com/mynetwork/network-manager/people-follow/followers/")

SCROLL_PAUSE_TIME = 5
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

links = soup.find_all('a', href = True)
for link in links:
    print(link['href'])

time.sleep(90)