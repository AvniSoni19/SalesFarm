from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# options= Options()
# options.headless=True
# options.add_argument('--headless')

s = Service('C:/Users/HITESH SONI/OneDrive/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s) #driver = webdriver.Chrome(service=s,options=options)
website = "https://www.naukri.com/react-js-developer-jobs-in-indore"
driver.get(website)
# driver.maximize_window()
driver.implicitly_wait(30)

container = driver.find_element(By.XPATH, "//div[contains(@class,'list')]")
tuples = container.find_elements(By.XPATH, "./article")

Job_Title = []
Company = []
Location = []

for tuple in tuples:
    title_element = tuple.find_element(By.XPATH, ".//a[contains(@class,'title ellipsis')]")
    company_element = tuple.find_element(By.XPATH, ".//a[contains(@class,'subTitle ellipsis fleft')]")
    location_element = tuple.find_element(By.XPATH, ".//span[contains(@class,'ellipsis fleft locWdth')]")

    Job_Title.append(title_element.text)
    Company.append(company_element.text)
    Location.append(location_element.text)

print(Job_Title)
print(Company)
print(Location)

driver.quit()