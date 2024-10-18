from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://in.indeed.com/jobs?q=react+js+developer&l=&vjk=22d160edf5c27b31")
while(True):
    pass