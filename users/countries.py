from bs4 import BeautifulSoup
import requests

url = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
req = requests.get(url)
countries = []

soup = BeautifulSoup(req.content, 'html.parser')
td = soup.find_all('td')
for country in range(1, 976, 5):
    countries.append(td[country].text)
new = tuple
countries_list = []


def get_countries():
    for i in countries:
        element1 = (i,)
        element2 = i
        new = element1 + (element2,)
        countries_list.append(new)
    return tuple(countries_list)
