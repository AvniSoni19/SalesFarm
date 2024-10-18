from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
website="https://linkedin.com/"
driver.get(website)
# sign=driver.find_element(By.XPATH,"""/html/body/div[1]/main/div/p/a""").click()
time.sleep(2)

email_input=driver.find_element(By.XPATH,"""/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input""")
email_input.send_keys("""nina.dob0989@gmail.com""")
pwd=driver.find_element(By.XPATH,"""/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input""")
pwd.send_keys("""letmylifeshine""")
signin=driver.find_element(By.XPATH,"""/html/body/main/section[1]/div/div/form/div[2]/button""").click()

sign=driver.find_element(By.XPATH,"""/html/body/div/header/div/div/nav/a[1]""").click()


#Login page details
email_input=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[1]/input""")
email_input.send_keys("""nina.dob0989@gmail.com""")
pwd=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[2]/input""")
pwd.send_keys("""letmylifeshine""")
sign_in=driver.find_element(By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[3]/button""").click()

time.sleep(2)
# driver.get(f'{website}/feed/')
# driver.save_screenshot("C:/Users/HITESH SONI/PycharmProjects/pythonProject1/ss.png")
while(True):
    pass
# https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F%3Ftrk%3D404_page&trk=login_reg_redirect
# driver.find_element(By.XPATH,"""Image ka XPATH""").screenshot(path)