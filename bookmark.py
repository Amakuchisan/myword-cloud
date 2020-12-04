import feedparser
import os
import re
import sys
from typing import List

# 公開しているブックマークの数を求める
def count_bookmark(hatena_id: str) -> int:
    d = feedparser.parse('https://b.hatena.ne.jp/{}/rss'.format(hatena_id))
    content = d['feed']['subtitle'] # 'Userのはてなブックマーク (num)'
    match = re.search(r"(はてなブックマーク \()(.*?)\)", content)
    num = match.group(2) # 公開しているブックマーク数
    if not num.isdecimal():
        print('Error: num is string', file=sys.stderr)
        return 0
    return int(num)

def get_title(hatena_id: str) -> List[str]:
    # 1ページに20件のデータがある。ページ数を求める
    bookmark_num = count_bookmark(hatena_id)
    max_page = (bookmark_num//20) + int((bookmark_num%20) > 0)

    titles = []

    for i in range(max_page):
        d = feedparser.parse('https://b.hatena.ne.jp/{}/rss?page={}'.format(hatena_id, i+1))
        entries = d['entries']
        for entry in entries:
            titles.append(entry['title'])
    return titles

hatena_id = os.environ['HATENAID']
titles = get_title(hatena_id)
print(titles)
