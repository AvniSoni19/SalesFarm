from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

s=Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://in.indeed.com/jobs?q=react+js+developer&l=&from=searchOnHP&vjk=2af53a6a9b1901c6")
time.sleep(5)

driver.find_element((By.XPATH,"/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/button")).click()
# while(True):
#      continue
# companies=driver.find_element(By.XPATH,"""/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[19]/div/div[1]/div[1]/div[2]/div[2]/span""")

# print(companies)

# driver.quit()

# driver.find_element_by_class_name('main-article')
# driver.find_element_by_class_name('plot')
# driver.find_element_by_class_name('full-script')
# driver.find_element_by_tag_name('span')
# driver.find_element_by_xpath('//tag[@AttributeName="Value"]')
# driver.find_elements_by_class_name('plot') --> gto find multiple elements from class