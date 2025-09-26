import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = sopa.select('img')
for imagen in imagenes:
    print(imagen['src'])