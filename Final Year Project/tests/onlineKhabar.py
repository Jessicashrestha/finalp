import requests
from bs4 import BeautifulSoup
import os
URL = "https://english.onlinekhabar.com/category/political"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
h3results = soup.select("div.listical-news-big  div.ok-post-contents > h2 > a")
print(h3results)
titles = []
titlesList = []
for atag in h3results:
    print(atag["href"])
    titlesList.append(atag.contents[0])
    titles.append("<a href=\""+atag["href"]+"\" target = \"_blank\">"+"<p>"+atag.contents[0]+"<p></a>")

titles = set(titles)
titlesList = set(titlesList)
# print(len(titles))
titles = list(titles)
titlesList = list(titlesList)
# print(titles)
titles = ''.join(titles)
print(titlesList)
print(titles)
import pickle
with open('THT.pkl', 'wb') as f:
    pickle.dump(titles, f)

finalList = []
for row in titlesList:
    finalList.append([row])

print(finalList)
import csv

# field names
fields = ['Headlines']

# data rows of csv file


with open('online.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(finalList)

    # for row in titlesList:
    #     write.writerow(row)