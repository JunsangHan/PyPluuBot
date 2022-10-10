# https://androidweekly.net/
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

url = "https://androidweekly.net/"
print(url)
response = requests.get(url)
if response.status_code != 200:
    print(response.status_code)
    quit()

html = response.text
soup = BeautifulSoup(html, "html.parser")
post_list = soup.find_all("div", {"class": "text-container galileo-ap-content-editor"})
for post in post_list:
    atag = post.find("a")
    if atag is not None:
        print(atag.string)
        print(atag["href"])

# TODO 추가적으로 타이틀 명 가져오기 및 하단 아티클 외 부분 제거 방법 고려 필요.
