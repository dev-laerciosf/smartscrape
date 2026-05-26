import re

import requests
from bs4 import BeautifulSoup, Tag

from smartscrape.models import Film

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}

# og:title vem como "The Matrix (1999)"
_TITLE_YEAR = re.compile(r"^(.+) \((\d{4})\)$")


def fetch_html(url: str) -> bytes:
    response = requests.get(url, headers=_HEADERS)
    response.raise_for_status()
    return response.content


def parse_film(html: bytes) -> Film:
    soup = BeautifulSoup(html, "html.parser")

    def meta_content(selector: str) -> str:
        tag = soup.select_one(selector)
        assert isinstance(tag, Tag), f"meta não encontrada: {selector}"
        content = tag.get("content")
        assert isinstance(content, str), f"meta sem content string: {selector}"
        return content

    title_year = meta_content('meta[property="og:title"]')
    match = _TITLE_YEAR.match(title_year)
    assert match is not None, f"formato inesperado de og:title: {title_year!r}"
    title, year = match.group(1), match.group(2)

    # twitter:data1 vem como "Lana Wachowski, Lilly Wachowski"
    director = meta_content('meta[name="twitter:data1"]')

    # twitter:data2 vem como "4.18 out of 5"
    average_rating = float(meta_content('meta[name="twitter:data2"]').split()[0])

    return Film(title=title, year=year, director=director, average_rating=average_rating)


def scrape_film(url: str) -> Film:
    return parse_film(fetch_html(url))
