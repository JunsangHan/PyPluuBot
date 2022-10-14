"""
https://github.com/google/ksp/releases/
https://github.com/google/dagger/releases/
https://github.com/gradle/gradle/releases/
"""
from scrapers import scraper
from database.database import Database
import sender.agit_sender as agit


class GithubReleaseScraper(scraper.Scraper):
    def __init__(self, url):
        super().__init__(url)

    def parse(self):
        super().parse()
        print("GithubReleaseScraper : " + str(self.url))
        if self.soup is None:
            print("error: self.soup is None")
            return

        db = Database()
        items = self.soup.find_all("a", {"class": "Link--primary"})
        for item in items:
            url_link = "https://github.com" + item["href"]
            title = item.string

            result = db.select(url_link)
            if result is None:
                print("DB has NOT this url")
                self.content_msg.append(agit.apply_h2(title) + url_link)
                db.insert(url_link, title)
            else:
                print("DB already has this url")

        return self.content_msg
