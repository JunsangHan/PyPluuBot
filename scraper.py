from abc import abstractmethod
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        self.soup = None
        self.url = url

    def request_html(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print(response.status_code)
            return None
        else:
            return response

    @abstractmethod
    def parse(self):
        """

        :return:
        """
        response = self.request_html()
        if response is None:
            self.soup = None
        else:
            self.soup = BeautifulSoup(response.text, "html.parser")
