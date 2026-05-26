import argparse
import json
from dataclasses import asdict

from smartscrape import __version__
from smartscrape.scraper import scrape_film


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="smartscrape",
        description="Extrai metadados de um filme do Letterboxd e imprime como JSON.",
    )
    parser.add_argument("url", help="URL da página do filme no Letterboxd")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    film = scrape_film(args.url)
    print(json.dumps(asdict(film), indent=2, ensure_ascii=False))
    return 0
