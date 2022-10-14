import sqlite3
import date_util as du


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("Post.db")
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS post_table (url text primary key, title text, date text);")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def select(self, url):
        result = self.cur.execute("SELECT * FROM post_table WHERE url = ?", (url,))
        return result

    def select_all(self):
        return self.cur.execute("SELECT * FROM post_table")

    def insert(self, url, title):
        try:
            self.cur.execute(
                "INSERT INTO post_table VALUES (?,?,?)",
                (
                    url,
                    title,
                    str(du.get_current_year()) + "-" + str(du.get_current_month()) + "-" + str(du.get_current_day())
                )
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Insert error")
