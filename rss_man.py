import feedparser
import requests
import bleach
import datetime


class RssReader():
    def __init__(self):
        self.__name__ = "RssReader"

    def get_feed(self, url): #-> feedparser.FeedParserDict
        result_set = requests.get(url)
        feed = feedparser.parse(result_set.text)
        return feed

    def sanitize(self, text): #-> string
        return bleach.clean(text, strip=True)

    def strip_html(self, html_str): #-> string
        """
        a wrapper for bleach.clean() that strips ALL tags from the input
        """
        tags = []
        attr = {}
        styles = []
        strip = True
        return bleach.clean(html_str,
                            tags=tags,
                            attributes=attr,
                            styles=styles,
                            strip=strip)

    def parse_feed(self, url): #-> list
        result = []
        feed = self.get_feed(url)
        for entry in feed["entries"]:
            result.append(
                {
                "title": entry.title.upper(),
                "summary": self.sanitize(self.strip_html(entry.description)),
                "url": entry.link,
                "pubdate": entry.published
                }
            )
        return result

    def format_published_date(self, string): #-> string
        return datetime.datetime.strptime(
            string,
            '%a, %d %b %Y %H:%M:%S %z'
            ).strftime('%A, %d-%b-%Y')
