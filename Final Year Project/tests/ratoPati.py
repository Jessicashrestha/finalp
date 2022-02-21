import csv

import requests
from bs4 import BeautifulSoup
import os

titles = []
titlesList = []
for i in range(1, 50):
    URL = "https://english.ratopati.com/category/international?page="+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    h3results = soup.select(".item-content > span > a")
    # print(h3results)


    for atag in h3results:
        # print(atag["href"])
        if " " in atag.contents[0].strip():
            # print(atag.contents[0].strip())
            titlesList.append(atag.contents[0].strip())

with open('countries.csv', 'w', encoding='UTF8', newline="") as f:
    writer = csv.writer(f)

    # write the header
    for title in titlesList:
        writer.writerow([title])

    # write the data

# print(titles)