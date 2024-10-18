from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://in.indeed.com/?from=gnav-jobsearch--indeedmobile")
time.sleep(2)
search_frame_1 = driver.find_element(By.XPATH,"""/html/body/div/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input""")
search_frame_1.send_keys("reactjs developer")
search_frame_1.send_keys(Keys.ENTER)
time.sleep(2)

while(True):
    pass