from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/home")
time.sleep(2)
login = driver.find_element(By.XPATH,"""/html/body/div[1]/header/nav/div/a[2]""").click()
time.sleep(2)
email_input=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[1]/input""")
email_input.send_keys("""nina.dob0989@gmail.com""")
pwd=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[2]/input""")
pwd.send_keys("""letmylifeshine""")
signin=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[3]/button""").click()

# email_input.send_keys(Keys.ENTER)
time.sleep(2)

while(True):
    pass