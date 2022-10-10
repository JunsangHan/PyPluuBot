# https://androidstudio.googleblog.com/
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

url = "https://androidstudio.googleblog.com/" + yearText + "/" + monthText + "/"
print(url)
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    quit()

html = response.text
soup = BeautifulSoup(html, "html.parser")

post_list = soup.find_all("div", {"class": "post"})
for post in post_list:
    ahref = post.find("a")["href"]
    print(ahref)
    print(post.find("a").string)

