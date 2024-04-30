import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    object_list = []
    objects = soup.find_all('div', {'class': "k-ad-card-wide v2"})
    for object in objects:
        link = object.find('a', attrs={'href': True})
        object_list.append({'Link': link['href']})
    return object_list


def scrap_page(base_url, start_page=1, max_pages=199):
    all_objects = []
    current_page = start_page
    while current_page <= max_pages:
        url = f'{base_url}{current_page}'
        print(f'Scraping page: {url}')
        html = fetch_page(url)
        if html:
            has_objects = parse_page(html)
            if has_objects:
                all_objects.extend(has_objects)
            else:
                print('No more objects founds')
        else:
            print('Failed to retrieve page')
            break
        current_page += 1
        sleep(1)

    df = pd.DataFrame(all_objects)
    print(df)
    df.describe()
    df.info()
    df.to_csv('kampas1.csv')


base_url = 'https://www.kampas.lt/namai?page='
scrap_page(base_url)
