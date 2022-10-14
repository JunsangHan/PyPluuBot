from scrapers.google.android_studio_scraper import AndroidStudioScraper
from scrapers.google.android_developers_scraper import AndroidDevelopersScraper
from scrapers.jetbrain_kotlin_scraper import JetbrainKotlinScraper

SCRAPERS = [
    AndroidStudioScraper("https://androidstudio.googleblog.com/"),
    AndroidDevelopersScraper("https://android-developers.googleblog.com/"),
    JetbrainKotlinScraper("https://blog.jetbrains.com/kotlin/")
]


def start():
    print("PluuBot Start")
    for scraper in SCRAPERS:
        scraper.parse()
