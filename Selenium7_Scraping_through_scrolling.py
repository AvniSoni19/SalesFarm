from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
website=""
driver.get(website)
height=driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
