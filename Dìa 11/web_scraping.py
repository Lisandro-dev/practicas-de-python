import bs4
import requests

url = "https://escueladirecta-blog.blogspot.com/"
response = requests.get(url)
sopa=bs4.BeautifulSoup(response.text, 'lxml')
print(sopa.select('h1')[0].getText())
listas=sopa.select('p')
print(listas)