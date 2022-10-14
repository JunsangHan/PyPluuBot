from scrapers.google.android_studio_scraper import AndroidStudioScraper
from scrapers.google.android_developers_scraper import AndroidDevelopersScraper
from scrapers.jetbrains_kotlin_scraper import JetbrainsKotlinScraper
import sender.agit_sender as agit

SCRAPERS = [
    AndroidStudioScraper("https://androidstudio.googleblog.com/"),
    AndroidDevelopersScraper("https://android-developers.googleblog.com/"),
    JetbrainsKotlinScraper("https://blog.jetbrains.com/kotlin/")
]

TITLE_TEXT = agit.apply_h1("밤새 올라온 안드로이드 소식 wit Pluu Bot")
DESCRIPTION_TEXT = agit.apply_hash_tag("Android") + " " + agit.apply_hash_tag("AndroidNews") + "\n\n"


def start():
    print("PluuBot Start")
    contents = []
    for scraper in SCRAPERS:
        messages = scraper.parse()
        if messages:
            for msg in messages:
                contents.append(msg)

    if not contents:
        print("PluuBot contents is empty")
        return

    send_msg = TITLE_TEXT + DESCRIPTION_TEXT
    for content in contents:
        send_msg = send_msg + "\n" + str(content) + "\n"

    print(send_msg)
    # TODO agit.send_msg


