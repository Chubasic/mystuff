#!/usr/bin/env python3
"""Created by Mighty_Noob"""

import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_dog_breeds")
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', class_="wikitable sortable")
breed = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    breed.append({
        'title': cols[3].a.text
    })


print(breed)
