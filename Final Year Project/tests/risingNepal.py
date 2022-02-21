import requests
from bs4 import BeautifulSoup
import os
URL = "https://risingnepaldaily.com/world"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

h3results = soup.select("a  p.trand")
# print(h3results)
titles = []
titlesList = []

for atag in h3results:
    # print(atag["href"])
    print(atag.contents[0].strip())
    titlesList.append(atag.contents[0])
# print(titles)