import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_object_data(url, headers):
    object = get_soup(url, headers)

    title = object.find('h1', class_='classified-title').text.strip()
    price = object.find('div', class_='price').text.strip().replace('\xa0', '').replace('€', '')

    place = object.find('p', class_='first-line')
    place = place.text.strip() if place else "N/A"

    span = object.find_all("span", class_="label")
    span0 = span[0].text.strip().replace(' m²: ', '').replace('Plotas', '') \
        if 0 < len(span) else "N/A"
    span1 = (span[1].text.strip().replace('€/m²: ', '').replace('€', '').
             replace('\xa0', '')) if 1 < len(span) else "N/A"
    span2 = span[2].text.strip().replace('Kambariai: ', '') if 2 < len(span) else "N/A"
    span3 = span[3].text.strip().replace('Aukštų skaičius ', '') if 3 < len(span)else "N/A"
    span4 = span[4].text.strip().replace('Konstrukcija: ', '') if 4 < len(span) else "N/A"
    span5 = span[5].text.strip().replace('Įrengimas: ', '') if 5 < len(span) else "N/A"
    span6 = span[6].text.strip().replace('Šildymas: ', '') if 6 < len(span) else "N/A"
    span7 = span[7].text.strip().replace('Statybų metai: ', '') if 7 < len(span) else "N/A"
    span8 = span[8].text.strip().replace('Sklypo plotas (a): ', '') if 8 < len(span) else "N/A"

    return {'Title': title, 'Price': price, 'Price €/m²': span1, 'Place': place,  'House area': span0,
            'Rooms No.': span2, 'Floors': span3, 'Contruction': span4, 'Installation': span5,
            'Heating': span6, 'Year of construction': span7, 'Land area (a)': span8}


def main():
    df_objects = pd.read_csv('kampas1.csv')
    objects_urls = 'https://www.kampas.lt' + df_objects['Link']
    objects_url_list = objects_urls.tolist()
    objects = []
    for url in objects_url_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
        details = get_object_data(url, headers)
        objects.append(details)
        print(details)
        sleep(1)

    df_all = pd.DataFrame(objects)
    df_all = df_all.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Price €/m²'], axis=1)
    print(df_all.info())
    print(df_all.describe())
    df_all.to_csv('nt_data_fin.csv')


if __name__ == '__main__':
    main()
