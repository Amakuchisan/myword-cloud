import feedparser
import re
import sys
from typing import List

class Bookmark:
    hatena_id = ""
    def __init__(self, hatena_id: str) :
        self.hatena_id = hatena_id

    # 公開しているブックマークの数を求める
    def count_bookmark(self) -> int:
        d = feedparser.parse('https://b.hatena.ne.jp/{}/rss'.format(self.hatena_id))
        content = d['feed']['subtitle'] # 'Userのはてなブックマーク (num)'
        match = re.search(r"(はてなブックマーク \()(.*?)\)", content)
        num = match.group(2) # 公開しているブックマーク数
        if not num.isdecimal():
            print('Error: num is string', file=sys.stderr)
            return 0
        return int(num)

    def get_title(self) -> List[str]:
        # 1ページに20件のデータがある。ページ数を求める
        bookmark_num = self.count_bookmark()
        max_page = (bookmark_num//20) + int((bookmark_num%20) > 0)

        titles = []

        for i in range(max_page):
            d = feedparser.parse('https://b.hatena.ne.jp/{}/rss?page={}'.format(self.hatena_id, i+1))
            entries = d['entries']
            for entry in entries:
                titles.append(entry['title'])
        return titles
