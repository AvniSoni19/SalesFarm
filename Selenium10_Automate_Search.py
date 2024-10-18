from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options= Options()
options.headless=True
options.add_argument('--headless')

chrome_driver_path = 'C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe'

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s,options=options)

df = pd.read_csv('naukri.com.csv')

Websites=[]

for com,loc in zip(df['Company'],df['Location']):
    com=''.join(com)
    search_string = f'site-{com}.com,{loc}'

    search_string = search_string.replace(' ', '+')


    driver.get(f"https://www.google.com/search?q={search_string}")

    link_string = com.replace(' ', '-').lower()
    # Xpath=f"//div[contains(@class,'yuRUbf')]//a[1]"
    link_element = driver.find_element(By.XPATH, f"//div[contains(@class,'yuRUbf')]/a[1]")
    link = link_element.get_attribute('href')
    Websites.append(link)
    print(link)
    time.sleep(15)


driver.quit()

df1=pd.DataFrame({"Websites":Websites})
df.to_csv("naukri1.com.csv", index=False)





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time
#
# options= Options()
# options.headless=True
# options.add_argument('--headless')
#
# chrome_driver_path = 'C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe'
#
# s = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=s,options=options)
#
# df = pd.read_csv('naukri.com.csv')
#
# Linkedin_links=[]
#
# for com, loc in zip(df['Company'], df['Location']):
#     search_string = f'{com} {loc} site:linkedin.com'
#
#     search_string = search_string.replace(' ', '+')
#
#
#     driver.get(f"https://www.google.com/search?q={search_string}&start=")
#
#     link_string = com.replace(' ', '-').lower()
#     Xpath=f"//div[contains(@class,'yuRUbf')]/a[contains(@href,{link_string})]"
#     link_element = driver.find_element(By.XPATH, f"//div[contains(@class,'yuRUbf')]/a[1]")
#     link = link_element.get_attribute('href')
#     Linkedin_links.append(link)
#     print(link)
#     time.sleep(10)
#
#
# driver.quit()
#
# df1=pd.DataFrame({"LinkedIn Links":Linkedin_links})
# df.to_csv("naukri1.com.csv", index=False)
#
