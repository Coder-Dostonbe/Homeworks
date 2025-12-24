import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

def parse_techno(category):
    tech_data = []

    load_dotenv()
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Linux; Android 6.0; '
                      'Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/143.0.0.0 Mobile Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='product-item-wrapper')
    for block in blocks:
        img_url = block.find('a', class_='product-link')
        images = img_url.find('img').get('data-src')
        title = block.find('h2').get_text()
        credit_price = block.find('div', class_='installment-price').get_text(strip=True)
        price = block.find('div', class_='product-price__current').get_text(strip=True)

        tech_data.append({
            'image': images,
            'title': title,
            'credit_price': credit_price,
            'price': price,
        })

        with open('noutbooks.json', 'w', encoding='utf-8') as file:
            json.dump(tech_data, file, ensure_ascii=False, indent=4)
parse_techno('katalog/noutbuki-asus/')