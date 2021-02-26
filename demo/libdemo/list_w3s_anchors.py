import requests
from bs4 import BeautifulSoup

website = "https://www.w3schools.com"
resp = requests.get(website)
bs = BeautifulSoup(resp.text,'html.parser')
anchors = bs.find_all("a")

links = set()
for a in anchors:
    href = a['href']
    if href.startswith("http"):
        links.add(href)
    else:
        links.add(website + href)

for link in links:
    print(link)
