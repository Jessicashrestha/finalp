import requests
from bs4 import BeautifulSoup
import os
URL = "https://thehimalayantimes.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

h3results = soup.select("h3.alith_post_title > a")
print(h3results)
titles = []
# titlesList = []

for atag in h3results:
    print(atag["href"])
    # titlesList.append(atag["title"])
    titles.append([atag["href"], atag["title"]])
# print(titles)
# print(len(titles))

# titles = set(titles)
# titlesList = set(titlesList)
# print(len(titles))
# titles = list(titles)
# titlesList = list(titlesList)
# print(titles)
# titles = ''.join(titles)
# print(titlesList)
print(titles)

# finalList = []
# for row in titlesList:
#     finalList.append([row])
#
# print(finalList)

import pickle
with open('THT.pkl', 'wb') as f:
    pickle.dump(titles, f)

