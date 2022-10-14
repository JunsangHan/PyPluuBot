# https://androidstudio.googleblog.com/
import scraper
import date_util as date
from sender.sender import Sender
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
        sender = Sender()
        post_list = self.soup.find_all("div", {"class": "post"})
        post_data_set = []
        for post_data in post_list:
            url_link = post_data.find("a")["href"]
            title = post_data.find("a").string.replace("\n", "")
            post_data_set.append(PostData(url_link, title))

            result = db.select(url_link)
            if result is None:
                print("DB has not this url")
                # TODO changer for your sender(e.g. Slack, Telegram..).
                sender.send_message(str(title) + "\n" + str(url_link), "YOUR_RECEIVER_URL")
                db.insert(url_link, title)
            else:
                print("DB already has this url")

            print("URL = " + str(url_link) + "\n" + "TITLE = " + title)

