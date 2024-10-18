from bs4 import BeautifulSoup
import requests
url="https://www.linkedin.com/jobs/search/"
result=requests.get(url)

content=result.text
soup=BeautifulSoup(content,"lxml")
# print(soup.prettify())
box = soup.find_all('div', {'class': 'job-card-container__company-name'})
company_name=[]
for name in box:
    company_name.append(name.text.strip())

print(company_name)