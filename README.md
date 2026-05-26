# smartscrape

Scraper que extrai metadados de filmes do Letterboxd (título, ano, diretor, nota média) a partir das meta tags da página.

## Instalação

```bash
pip install -e .
```

Após instalar, o comando `smartscrape` fica disponível em qualquer diretório.

## Uso

```bash
smartscrape https://letterboxd.com/film/the-matrix/
```

## Exemplo de output

```bash
$ smartscrape https://letterboxd.com/film/parasite-2019/
{
  "title": "Parasite",
  "year": "2019",
  "director": "Bong Joon Ho",
  "average_rating": 4.53
}
```

## Desenvolvimento

```bash
pip install -e ".[dev]"
```
