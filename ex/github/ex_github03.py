# https://github.com/gradle/gradle/releases/
import requests
from bs4 import BeautifulSoup

url = "https://github.com/gradle/gradle/releases/"
print(url)
response = requests.get(url)
if response.status_code != 200:
    print(response.status_code)
    quit()

html = response.text
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("a", {"class": "Link--primary"})
for item in items:
    print(item.string)
    print("https://github.com" + item["href"])