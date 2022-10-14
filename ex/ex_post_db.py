# https://androidstudio.googleblog.com/
import requests
from bs4 import BeautifulSoup
import datetime
from ex.PostTestData import PostTestData
import sqlite3

# DB connection
conn = sqlite3.connect("Post.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS PostDataTable(url text primary key, title text, date text);")

# Scraping
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
post_data_set = []
for post_data in post_list:
    url_ahref = post_data.find("a")["href"]
    title = post_data.find("a").string.replace("\n", "")
    post_data_set.append(PostTestData(url_ahref, title))

    cur.execute("SELECT * FROM PostDataTable WHERE url = ?", (url_ahref, ))
    result = cur.fetchone()
    if result is None:
        print("DB result is None")
        # TODO #1 send this post to Agit.
        # TODO #2 insert this post to database after sending it.
    else:
        print("DB already has this Url")
    # print("DB > " + str(cur.fetchone()))


# for post_data in post_data_set:
#     print(post_data)
#     try:
#         cur.execute(
#             "INSERT INTO PostDataTable VALUES (?,?,?)",
#             (
#                 post_data.url,
#                 post_data.title,
#                 str(now.year) + "-" + str(now.month) + "-" + str(now.day)
#             )
#         )
#     except sqlite3.IntegrityError:
#         print("INSERT ERROR")

# For database debugging.
for item in cur.execute("SELECT * FROM PostDataTable"):
    print(item)

conn.commit()
conn.close()
