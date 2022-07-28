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

    # params = {
    #     'q': '',
    #     'rlz': '1C1GCEA_enIR1014IR1014',
    #     'oq': 'book',
    #     'aqs': 'chrome.1.69i57j69i59j35i39l2j0i512l3j46i199i465i512j0i512j46i199i457i465i512.5312j0j1',
    #     'sourceid' : 'chrome',
    #     'ie': 'UTF - 8'
    # }

    # headers = {
    #
    #     'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
    #     'accept - language': 'en - US, en - GB;q = 0.9, en;q = 0.8, fa - IR;q = 0.7, fa;q = 0.6',
    #     'cache - control': 'max - age = 0',
    #     'cookie': 'SID = MwiVNVLb8nqXZ7pqj5ny1ZfM - X2qcmKviFZamnCMS_QdfNauY_xGVOxl_SqNGpBVL - 7iEA.;__Secure - 1PSID = MwiVNVLb8nqXZ7pqj5ny1ZfM - X2qcmKviFZamnCMS_QdfNauZ - DU6QlioZJgd4JOsBHouQ.;__Secure - 3PSID = MwiVNVLb8nqXZ7pqj5ny1ZfM - X2qcmKviFZamnCMS_QdfNauFYjGwzLoi_4fddKJyhTxIw.;HSID = AhYEXwBURzO48_Evy;SSID = A0HwPbYtIRvZb2hWr;APISID = d - T0Mnkfa7ZWFbDN / ABdBi3Sk17khx0OKr;SAPISID = 9wEuRjC3 - mBSVLBV / A0ClEYJ3jPxEOruUo;__Secure - 1PAPISID = 9wEuRjC3 - mBSVLBV / A0ClEYJ3jPxEOruUo;__Secure - 3PAPISID = 9wEuRjC3 - mBSVLBV / A0ClEYJ3jPxEOruUo;SEARCH_SAMESITE = CgQI_5UB;AEC = AakniGMrwfvKfmdiMMhO_dxy7PIdJR0R - t7Dz6dsGvh4NKzTh4iU9uWzuWg;NID = 511 = T2cd7FN2MPDSmchmmvnTP1NcLCTKY02smhmp7O7QtQM0OGq2Ebim6 - lQdLXkVxj6 - -cQFPxkhhRYv5542rlMnJGtdZxAUo15bjBUfkrxzPbbPLzBuabN5JNKRnooWcqgu_9hIduqBGtafaHkLBTrDc - NABNt82PKi1Y_9AKBchZa1VBEf9ZDStkjiFYs2d9KkcY - Z1_x - iRFHUWcIXfH1TRaZGb_GLjhyY_iOygj1vZSnnjQgngfG7Ld;1P_JAR = 2022 - 07 - 26 - 07;DV = Q_VZne75Q1NRwMb7DvWOPzOSLYSWI5hw4P5MyRCtgwEAAMDXZOvQycoV3wAAAICIXxvmwpdnQwAAAB7d8Xg8VY - nFQAAAA;SIDCC = AJi4QfHqF_4ouC8uVhlCadE9_2ob7TL5TicCT7Xf4MvOVbB49t - yECPa5RZXsDj7PK8N65BoHQ;__Secure - 1PSIDCC = AJi4QfEBtGnPpGOlOhyrAAGC1KaCYahbkfYOFi8_7dxWMEmjTT3Z7rukQL - ZQA4FuO0O21G8UA;__Secure - 3PSIDCC = AJi4QfFgd415Z_tYn429PNmsk7VYp49etJ07lJtywd9ck8ydig3nSuiNSn4mFUAUf2BAavsp4A',
    #     'referer': 'https: // www.google.com /',
    #     'upgrade - insecure - requests': '1',
    #     'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 103.0.0.0Safari / 537.36'
    # }

    # def fetch(self, query):
    #     self.params['q'] = query
    #     response = requests.get(self.base_url, self.params)
    #     self.store_response(response)

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

            # titles = content.findAll('div', {'class': 'BNeawe vvjwJb AP7Wnd'})
            # for title in titles:
            #     print(title.text)
            #
            # print('--------------------------------------------------------')
            #
            # links = content.findAll('div', {'class': 'BNeawe UPmit AP7Wnd'})
            # for link in links:
            #     print(link.text)
            #
            # print('--------------------------------------------------------')


            # for desc in content.find_all('div', {'class': 'kCrYT'}):
            #     print(desc.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).text)

            # desc = content.find('div', {'class': 'kCrYT'})


            # descriptions = content.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})

            # descriptions = content.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
            # for description in descriptions:
            #     print(description.text)

            # info = [[title],[link],[description]]
            # thewriter.writerow(info)


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

