import requests
from bs4 import BeautifulSoup

url ="https://www.cafe-amazon.com/products.aspx?Lang=TH&PageID=3"
web = requests.get(url)

soup = BeautifulSoup(web.text, 'html.parser')
find_word = soup.find_all("td")

#for factory in find_word:
    #factory = str(factory).split('td')[1]
    #factory = str(factory).split('td')[0]
print(soup)

