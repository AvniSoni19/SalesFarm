from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://in.indeed.com/jobs?q=react+js+developer&l=&from=searchOnHP&vjk=2af53a6a9b1901c6")
driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/button").click()
time.sleep(2)

while(True):
    pass


