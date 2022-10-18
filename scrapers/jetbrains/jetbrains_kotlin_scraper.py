# https://blog.jetbrains.com/kotlin/
from scrapers import scraper
import date_util as date
from data import PostData
from database.database import Database
import sender.agit_sender as agit


class JetbrainsKotlinScraper(scraper.Scraper):
    def __init__(self, url):
        super().__init__(url)
        self.url = date.make_url_with_current_year_month(self.url)

    def parse(self):
        super().parse()
        print("JetbrainsKotlinScraper : " + str(self.url))
        if self.soup is None:
            print("error: self.soup is None")
            return

        db = Database()
        posts = []
        new_post = self.soup.find("div", {"class": "promo__row"})
        if new_post is not None:
            posts.append(PostData(new_post.find("a")["href"], new_post.find("h1").string.replace("\n", "")))

        columns = self.soup.find_all("div", {"class": "col"})
        for col in columns:
            url_link = col.find("a")["href"]
            title = col.find("h3").string.replace("\n", "")
            posts.append(PostData(url_link, title))

        for post in posts:
            url_link = post.url
            title = post.title

            result = db.select(url_link)
            if result is None:
                print("DB inserts this url : " + url_link)
                self.content_msg.append(agit.apply_h2(title) + url_link)
                db.insert(url_link, title)

        return self.content_msg
