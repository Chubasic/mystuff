#!/usr/bin/env python3
"""Created by Mighty_Noob"""

import urllib.request
from bs4 import BeautifulSoup


base_url = "https://en.wikipedia.org/wiki/List_of_dog_breeds"

def main():
	parse(get_html(base_url))



def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find('table', {'class':'wikitable sortable'})

	projects = []

	for row in table.find_all('tr'):
		cols = row.find_all('td')
		projects.append({
			'title': cols[0].a.text
		})
		return projects

if __name__ == '__main__':
	main()
