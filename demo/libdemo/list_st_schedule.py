import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com/"
resp = requests.get(website)
bs = BeautifulSoup(resp.text,'html.parser')
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    print(f"{cols[0].text:40} {cols[1].text:20} {cols[2].text:}")






