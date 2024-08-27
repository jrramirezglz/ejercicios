import bs4
import requests
#extraer titulo de la pagina
url = 'https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html'
resultado = requests.get(url)
print(type(resultado))
print(resultado.text)
sopa = bs4.BeautifulSoup(resultado.text,'lxml')
print(sopa)
print(sopa.select('title'))
print(sopa.select('p'))
print(len(sopa.select('p')))
print(sopa.select('title')[0].get_text())
parrafo_especial = sopa.select('p')
print(parrafo_especial[3].get_text())