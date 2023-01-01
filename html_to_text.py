import requests
import bs4
import asyncio


class HtmlToText:
    def __init__(self, url: str, element: str, attr: dict = None):
        self.url = url
        self.element = element
        self.attr = attr
        self.tag_res = []
        self.getter = None
        self.soup = None
        self.page = None

    async def get_html_tags(self):
        self.page = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.page.text, "html.parser")

        content = self.soup.find_all(name=self.element, attrs=self.attr)
        for tag in content:

            line = str(tag.contents[0]).replace("\n", " ").strip()
            if line.startswith("<"):
                continue

            self.tag_res.append(line)

        return self.tag_res
