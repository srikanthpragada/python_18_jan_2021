import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com/"
resp = requests.get(website)
bs = BeautifulSoup(resp.text,'html.parser')
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
print(table)

