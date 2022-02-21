import requests
from bs4 import BeautifulSoup
import os
URL = "https://nepaliheadlines.com/news/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

h3results = soup.select("h2 > a")
# print(h3results)
titles = []
titlesList = []

for atag in h3results:
    # print(atag["href"])
    print(atag.contents[0])
    titlesList.append(atag.contents[0])
# print(titles)