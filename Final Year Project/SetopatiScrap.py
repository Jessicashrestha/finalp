import requests
from bs4 import BeautifulSoup
import os
URL = "https://en.setopati.com/"
page = requests.get(URL)
# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
h3results = soup.select("#content div.items > a")
notInList = ["https://en.setopati.com/view", "https://en.setopati.com/blog", "https://en.setopati.com/literature", "https://en.setopati.com/readers-opinion"]
# print(h3results)
titles = []
titlesList = []
for atag in h3results:
    if str(atag["href"]) in notInList:
        continue
    title = atag.select("  span.main-title")[0].contents[0]
    # print(type(title))
    if (title == '\n'):
        continue
    print(str(atag["href"]))
    # titlesList.append(str(title))
    titles.append([atag["href"],str(title)])

# titles = set(titles)
# titlesList = set(titlesList)
# titles = list(titles)
# titlesList = list(titlesList)
# titles = ''.join(titles)
print(titles)
# print(titlesList)
# finalList = []
# for row in titlesList:
#     finalList.append([row])

# print(finalList)
import pickle
with open('setopati.pkl', 'wb') as f:
    pickle.dump(titles, f)



