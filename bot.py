import json
import re
import sys

import requests
from bs4 import Tag
from bs4 import BeautifulSoup

url = sys.argv[1]
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')


def meta_content(selector: str) -> str:
    tag = soup.select_one(selector)
    assert isinstance(tag, Tag), f"meta não encontrada: {selector}"
    content = tag.get("content")
    assert isinstance(content, str), f"meta sem content string: {selector}"
    return content


# og:title vem como "The Matrix (1999)"
title_year = meta_content('meta[property="og:title"]')
match = re.match(r"^(.+) \((\d{4})\)$", title_year)
assert match is not None, f"formato inesperado de og:title: {title_year!r}"
title, year = match.group(1), match.group(2)

# twitter:data1 vem como "Lana Wachowski, Lilly Wachowski"
director = meta_content('meta[name="twitter:data1"]')

# twitter:data2 vem como "4.18 out of 5"
rating = float(meta_content('meta[name="twitter:data2"]').split()[0])

data = {
    "title": title,
    "year": year,
    "director": director,
    "average_rating": rating,
}

print(json.dumps(data, indent=2))