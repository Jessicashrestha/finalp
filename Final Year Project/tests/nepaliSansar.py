import requests
from bs4 import BeautifulSoup
import os
URL = "https://www.nepalisansar.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

h3results = soup.select("div.art_title > a")
# print(h3results)
titles = []
titlesList = []

for atag in h3results:
    # print(atag["href"])
    titlesList.append(atag.contents[0])
    titles.append("<a href=\""+atag["href"]+"\" target = \"_blank\">"+"<p>"+atag.contents[0]+"<p></a>")
# print(titles)
# print(len(titles))

titles = set(titles)
titlesList = set(titlesList)
# print(len(titles))
titles = list(titles)
titlesList = list(titlesList)
# print(titles)
titles = ''.join(titles)
print(titlesList)
print(titles)


finalList = []
for row in titlesList:
    finalList.append([str(row).replace("\n", "")])

print("the list", finalList)



import pickle
with open('nepaliSansar.pkl', 'wb') as f:
    pickle.dump(titles, f)


import csv
fields = ['Headlines']

# data rows of csv file


with open('nepali.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(finalList)
