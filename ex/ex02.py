# https://blog.jetbrains.com/kotlin/
import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
yearText = str(now.year)
month = now.month
if month < 10:
    monthText = "0" + str(month)
else:
    monthText = str(month)

url = "https://blog.jetbrains.com/kotlin/" + yearText + "/" + monthText + "/"
print("URL : " + url)
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    quit()

html = response.text
soup = BeautifulSoup(html, "html.parser")

promo_row = soup.find("div", {"class": "promo__row"})
print("- New post- ")
print(promo_row.find("a")["href"])
print(promo_row.find("h1").string)

print("- Latest posts- ")
cols = soup.find_all("div", {"class": "col"})
for col in cols:
    ahref = col.find("a")["href"]
    title = col.find("h3").string
    print(ahref)
    print(title)
