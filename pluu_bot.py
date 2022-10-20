from scrapers.google.android_studio_scraper import AndroidStudioScraper
from scrapers.google.android_developers_scraper import AndroidDevelopersScraper
from scrapers.jetbrains.jetbrains_kotlin_scraper import JetbrainsKotlinScraper
from scrapers.github.github_release_scraper import GithubReleaseScraper
import sender.agit_sender as agit
import urllib3
import datetime

SCRAPERS = [
    AndroidStudioScraper("https://androidstudio.googleblog.com/"),
    AndroidDevelopersScraper("https://android-developers.googleblog.com/"),
    JetbrainsKotlinScraper("https://blog.jetbrains.com/kotlin/"),
    GithubReleaseScraper("https://github.com/google/ksp/releases/", "Ksp"),
    GithubReleaseScraper("https://github.com/google/dagger/releases/", "Dagger"),
    GithubReleaseScraper("https://github.com/gradle/gradle/releases/", "Gradle"),
    GithubReleaseScraper("https://github.com/bumptech/glide/releases/", "Glide"),
    GithubReleaseScraper("https://github.com/material-components/material-components-android/releases/",
                         "Material Components Android"),
]

TITLE_TEXT = agit.apply_h1("밤새 올라온 안드로이드 소식 wit Pluu Bot")
DESCRIPTION_TEXT = agit.apply_hash_tag("Android") + " " + agit.apply_hash_tag("AndroidNews") + "\n\n"


def start():
    print("PluuBot Start " + str(datetime.datetime.now()))
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
    urllib3.disable_warnings()
    agit.send_message(send_msg)


