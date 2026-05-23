# smartscrape

Scraper que extrai metadados de filmes do Letterboxd (título, ano, diretor, nota média) a partir das meta tags da página.

## Uso

```bash
python smartscrape.py https://letterboxd.com/film/the-matrix/
```

## Exemplo de output

```bash
$ python smartscrape.py https://letterboxd.com/film/parasite-2019/
{
  "title": "Parasite",
  "year": "2019",
  "director": "Bong Joon Ho",
  "average_rating": 4.53
}
```
