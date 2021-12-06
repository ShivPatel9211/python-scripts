import requests
from bs4 import BeautifulSoup

# url=r'https://www.myntra.com/women-shrugs'
url2=r'https://constant.myntassets.com/web/assets/js/main.f0ff456bfcc2a473639f.js'
r = requests.get(url2)
htmlContent=r.content

soup =BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
# print(url)