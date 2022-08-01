import requests
from bs4 import BeautifulSoup
from csv import writer
import csv
from io import StringIO

import json
import re
from lxml.html import fromstring



class GoogleScraper:
    base_url = 'https://www.google.com/search'

    params = {

        'q': 'book',
        'rlz': '1C1GCEA_enIR1014IR1014',
        'oq': 'book',
        'aqs': 'chrome.0.69i59l2j35i39j46i67i199i457i465j0i67j0i512l5.1035j0j1',
        'sourceid': 'chrome',
        'ie': 'UTF - 8'
    }

   
    def find_tag(self):
        self.params['q'] = "sports"
        response = requests.get(self.base_url, self.params)
        self.store_response(response)
        html = self.load_response()
        content = BeautifulSoup(html, 'html.parser')

        with open('SearchResultsPage.csv', 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['Title', 'Link', 'Description']
            thewriter.writerow(header)

            title = [title.text for title in content.findAll('div', {'class': 'BNeawe vvjwJb AP7Wnd'})]
            link = [link.text for link in content.findAll('div', {'class': 'BNeawe UPmit AP7Wnd'})]
            description = [description.text for description in content.findAll('div', {'class': 'BNeawe s3v9rd AP7Wnd'})]

            desc = []
            for i in range(0, len(description)):
                if i % 2:
                    desc.append(description[i])


            for i in range(9):
                info = [title[i],link[i],desc[i]]
                thewriter.writerow(info)



    def store_response(self, response):
        if response.status_code == 200:
            print('Saving response to "res.html"', end="")

            with open('res.html', 'w') as html_file:
               html_file.write(response.text)

            print('Done')
        else:
            print('Bad response!')
            print(response.status_code)

    def load_response(self):
        html = ''

        with open('res.html', 'r') as html_file:
            for line in html_file.read():
                html += line

        return html


    # def run(self):
    #     # response = self.fetch('book')
    #     # self.store_response(response)
    #
    #     html = self.load_response()
    #     self.find_tag(html)

if __name__ == '__main__':
    scraper = GoogleScraper()
    # scraper.run()
    scraper.find_tag()

