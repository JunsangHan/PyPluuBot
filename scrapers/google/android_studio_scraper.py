# https://androidstudio.googleblog.com/
import scraper
import date_util as date
from data import PostData
from database.database import Database


class AndroidStudioScraper(scraper.Scraper):
    def __init__(self, url):
        super().__init__(url)
        self.url = date.make_url_with_current_year_month(self.url)

    def parse(self):
        super().parse()
        if self.soup is None:
            print("error: self.soup is None")
            return

        db = Database()
        post_list = self.soup.find_all("div", {"class": "post"})
        post_data_set = []
        for post_data in post_list:
            url_ahref = post_data.find("a")["href"]
            title = post_data.find("a").string.replace("\n", "")

            post_data_set.append(PostData(url_ahref, title))

            result = db.select(url_ahref)
            if result is None:
                print("DB has not this url")
                # TODO #1 send this post to Agit.
                # TODO #2 insert this post to database after sending it.
            else:
                print("DB already has this url")

            print("URL = " + str(url_ahref) + "\n" + "TITLE = " + title)

