from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

Job_Title = []
Company = []
Location = []

s = Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)


website = "https://in.indeed.com/jobs?q=react+js+developer&l=Indore&from=searchOnHP&vjk=c8e360c68e612728"
driver.get(website)
driver.maximize_window()
driver.implicitly_wait(30)

# Pagination
pagination = driver.find_element(By.XPATH, "//nav[contains(@class,'css-jbuxu0 ecydgvn0')]")
pages = pagination.find_elements(By.TAG_NAME, "div")
last_page = int(pages[-2].text)
next_page = driver.find_element(By.XPATH, "//a[contains(@data-testid,'pagination-page-next')]")
# next_page_text=next_page.text



current_page = 1
while current_page <= last_page:
        time.sleep(2)
        time.sleep(2)

        container = driver.find_element(By.XPATH, "//ul[contains(@class,'jobsearch-ResultsList css-0')]")
        tuples = container.find_elements(By.XPATH, "//td[contains(@class,'resultContent')]")

        for tuple in tuples:
            title_element = tuple.find_element(By.XPATH, ".//h2[contains(@class,'jobTitle')]")
            company_element = tuple.find_element(By.XPATH, ".//span[contains(@class,'companyName')]")
            location_element = tuple.find_element(By.XPATH, ".//div[contains(@class,'companyLocation')]")

            Job_Title.append(title_element.text)
            Company.append(company_element.text)
            Location.append(location_element.text)


        driver.execute_script("arguments[0].click();", next_page)
        current_page += 1
        print(Job_Title)
        print(Company)
        print(Location)

driver.quit()

df = pd.DataFrame({"Job Title": Job_Title, "Company": Company, "Location": Location})
df.to_csv("indeed.csv", index=False)

