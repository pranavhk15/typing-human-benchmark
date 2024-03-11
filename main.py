from bs4 import BeautifulSoup
import pyautogui
from selenium import webdriver
import time

browswer = webdriver.Chrome()

url = "https://humanbenchmark.com/tests/typing"
browswer.get(url)

page_source = browswer.page_source
soup = BeautifulSoup(page_source, 'html.parser')

spans = soup.find_all('span', class_="incomplete")
text = "".join([s.get_text() for s in spans])


time.sleep(2)

pyautogui.write(text, interval=0)

time.sleep(10)

browswer.quit()