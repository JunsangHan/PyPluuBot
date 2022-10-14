# https://blog.jetbrains.com/kotlin/
import scraper
import date_util as date


class JetbrainKotlinScraper(scraper.Scraper):
    def __init__(self, url):
        super().__init__(url)
        self.url = date.make_url_with_current_year_month(self.url)

    def parse(self):
        print("JetbrainKotlinScraper : " + str(self.url))
