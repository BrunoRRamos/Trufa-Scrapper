import sys
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from constants import HEADER

def scrapParfum(target_url):
    url = target_url
    request = Request(url, headers=HEADER)
    response = urlopen(request)

    html_bytes = response.read()
    encoding = response.headers.get_content_charset()

    if encoding is None:
        encoding = 'utf-8'

    html = html_bytes.decode(encoding, errors='replace')

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find(id='product-name').get_text().strip()
    price = soup.find(id='price_display').get_text().strip()
    isAvailable = soup.find('div', class_='product-label product-detail-label label-light js-stock-label pull-left m-top-none m-bottom-quarter m-right-quarter m-bottom-xs').get_text().strip()

    return { 'name': name, 'price': price, 'isAvailable': isAvailable }


parfuns = ['https://www.thekingofparfums.com.br/produtos/giorgio-armani-acqua-di-gio-profondo-lancamento/', 
                  'https://www.thekingofparfums.com.br/produtos/paco-rabanne-1-million-royal/',
                  'https://www.thekingofparfums.com.br/produtos/invictus-paco-rabanne/' ]

for url in parfuns:
    obj = scrapParfum(url)

    print(obj['name'])
    print(obj['price'])
    print(obj['isAvailable'])