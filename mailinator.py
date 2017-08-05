#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import codecs
import json
# from collections import defultdict

# A dict to store the alternate domains and their frequency
alternate_domains = {}


# Makes a reques to the mailinator website and get the webpage
def make_request():
    url = "https://www.mailinator.com/"
    r = requests.get(url)
    return r.text


# extract the domain name from the mailinator webpage
def extract_data(page):
    soup = BeautifulSoup(page, 'lxml')
    div = soup.find_all('div', class_="col-sm-5 pull-right")
    mylist = [x.strip() for x in div[0].text.split('@')]
    if str(mylist[1]) in alternate_domains:
        alternate_domains[str(mylist[1])] += 1
    else:
        alternate_domains[str(mylist[1])] = 1


#
# def load_data():
#     f = codecs.open('mailinator_domains.txt')


# The default function
if __name__ == "__main__":
    for i in range(100):
        page = make_request()
        extract_data(page)

    with codecs.open('mailinator_domains.txt', 'a') as f:
        sum = 0
        for key in alternate_domains:
            sum += alternate_domains[key]
        # f.write(json.dumps(alternate_domains, indent=2) + "\n")
        f.write(json.dumps(alternate_domains) + "\n")
