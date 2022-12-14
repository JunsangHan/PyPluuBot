# https://androidstudio.googleblog.com/
from scrapers import scraper
import date_util as date
from database.database import Database
import sender.agit_sender as agit


class AndroidStudioScraper(scraper.Scraper):
    def __init__(self, url):
        super().__init__(url)
        self.url = date.make_url_with_current_year_month(self.url)

    def parse(self):
        super().parse()
        print("AndroidStudioScraper : " + str(self.url))
        if self.soup is None:
            print("error: self.soup is None")
            return

        db = Database()
        posts = self.soup.find_all("div", {"class": "post"})
        for post in posts:
            url_link = post.find("a")["href"]
            title = post.find("a").string.replace("\n", "")

            result = db.select(url_link)
            if result is None:
                print("DB inserts this url : " + url_link)
                self.content_msg.append(agit.apply_h2(title) + url_link)
                db.insert(url_link, title)

        return self.content_msg
