import requests
from bs4 import BeautifulSoup


def parser_travel(categories):
    parsed_data = []

    BASE_URL = "https://books.toscrape.com/"
    category_path = "catalogue/category/books/travel_2/index.html"
    full_url = BASE_URL + category_path

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(full_url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    blocks = soup.find_all('article', class_='product_pod')


    for block in blocks:
        img_tag = block.find('img')
        image_relative = img_tag['src']
        image = image_relative.replace('../../..', '')
        full_image = BASE_URL + image if image.startswith('/media') else BASE_URL + '/catalogue' + image
        title_tag = block.find('h3').find('a')
        title = title_tag['title'] if 'title' in title_tag.attrs else title_tag.get_text(strip=True)
        price_tag = block.find('p', class_='price_color')
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        avail_tag = block.find('p', class_='instock availability')
        availability = avail_tag.get_text(strip=True).strip() if avail_tag else "N/A"

        parsed_data.append({
            'title': title,
            'price': price,
            'availability': availability,
            'image': full_image,
            'product_url': BASE_URL + 'catalogue/' + title_tag['href']
        })

    return parsed_data


parser_travel('catalogue/category/books/travel_2/index.html')

