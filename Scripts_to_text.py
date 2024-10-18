from bs4 import BeautifulSoup
import requests

website = "https://subslikescript.com"
url = f'{website}/movies'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content, "lxml")

# pagination
pagination=soup.find('ul',class_='pagination')
pages=pagination.find_all('li',class_='page-item')
last_page=pages[-2].text

links = []

for page in range(1,int(last_page)+1):
    # https://subslikescript.com/movies?page=4
    url=f'{website}/movies?page={page}'
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find('article', class_='main-article')



    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
           print(link)
           url = f'{website}/{link}'
           result = requests.get(url)
           content = result.text
           soup = BeautifulSoup(content, "lxml")

           box = soup.find('article', class_='main-article')
           title_element = box.find('h1')
           if title_element is not None:
               title = title_element.get_text()
               transcript_box = box.find('div', class_='full-script')
               if transcript_box is not None:
                   transcript = transcript_box.get_text()

                   try:
                       with open(f'{title}.txt', 'w') as file:
                           file.write(transcript)
                   except Exception as e:
                       print(f"Error occurred while writing {title}.txt: {e}")
               else:
                   print(f"No transcript found for {title}.")
           else:
               print(f"No title found for the link: {link}")
        except:
            print(link)
            print("This given link is not working")




# title=box.find('h1').get_text()
# print(title)
# transcript=box.find('div',class_='full-script')
# print(transcript.get_text())
# print(title,'\n')
# script=box.get_text('\n')
# print(script)

# with open(f'{title}.txt','w') as file:
#     file.write(script)