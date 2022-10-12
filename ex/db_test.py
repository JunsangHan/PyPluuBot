import sqlite3

conn = sqlite3.connect('Post.db')
cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS PostDataTable(url text primary key, title text, date text);")
# cur.execute("DROP TABLE PostData")
conn.close()

