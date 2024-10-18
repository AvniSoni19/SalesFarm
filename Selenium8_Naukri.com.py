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


website = "https://www.naukri.com/node-js-developer-jobs-in-dubai?k=node%20js%20developer&l=dubai"
driver.get(website)
driver.maximize_window()
driver.implicitly_wait(30)

# Pagination
pagination = driver.find_element(By.XPATH, "//div[contains(@class,'pagination lastCompMark')]")
pages = pagination.find_elements(By.TAG_NAME, "a")
last_page = int(pages[-2].text)

current_page = 1
while current_page <= last_page:
    time.sleep(2)
    time.sleep(2)
    container = driver.find_element(By.XPATH, "//section[contains(@class,'listContainer fleft')]")
    tuples = container.find_elements(By.XPATH, "./div[contains(@class,'list')]/article")

    for tuple in tuples:
        title_element = tuple.find_element(By.XPATH, ".//a[contains(@class,'title ellipsis')]")
        company_element = tuple.find_element(By.XPATH, ".//a[contains(@class,'subTitle ellipsis fleft')]")
        location_element = tuple.find_element(By.XPATH, ".//span[contains(@class,'ellipsis fleft locWdth')]")

        Job_Title.append(title_element.text)
        Company.append(company_element.text)
        Location.append(location_element.text)

    next_page = driver.find_element(By.XPATH, "//a[contains(@class,'fright fs14 btn-secondary br2')]")
    driver.execute_script("arguments[0].click();", next_page)
    current_page += 1

driver.quit()

df = pd.DataFrame({"Job Title": Job_Title, "Company": Company, "Location": Location})
df.to_csv("naukri1.com.csv", index=False)


########### CHAT GPT #############

# from bs4 import BeautifulSoup
# import openpyxl
#
# # Read the HTML file
# with open('naukri2.html', 'r') as file:
#     html_data = file.read()
#
# # Create BeautifulSoup object
# soup = BeautifulSoup(html_data, 'html.parser')
#
# # Find all articles with class="jobTuple"
# articles = soup.find_all('article', class_='jobTuple')
#
# # Initialize empty lists
# Job_Title = []
# Company = []
# Location = []
#
# # Extract information from each article
# for article in articles:
#     # Extract Job Title
#     try:
#         job_title = article.find('a', class_='title ellipsis').text.strip()
#     except AttributeError:
#         job_title = ''
#     Job_Title.append(job_title)
#
#     # Extract Company
#     try:
#         company = article.find('a', class_='subTitle ellipsis fleft').text.strip()
#     except AttributeError:
#         company = ''
#     Company.append(company)
#
#     # Extract Location
#     try:
#         location = article.find('span', class_='ellipsis fleft locWdth').text.strip()
#     except AttributeError:
#         location = ''
#     Location.append(location)
#
# # Create a new Excel file
# wb = openpyxl.Workbook()
# ws = wb.active
#
# # Write headers
# ws['A1'] = 'Job_Title'
# ws['B1'] = 'Company'
# ws['C1'] = 'Location'
#
# # Write data to Excel file
# for i in range(len(Job_Title)):
#     ws.cell(row=i + 2, column=1, value=Job_Title[i])
#     ws.cell(row=i + 2, column=2, value=Company[i])
#     ws.cell(row=i + 2, column=3, value=Location[i])
#
# # Save the Excel file
# wb.save('jobs2.xlsx')
#
