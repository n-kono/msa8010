import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import string


def get_street_abbv():
    headers = {
    'User-Agent': '',
    }

    abbv = BeautifulSoup(requests.get('https://pe.usps.com/text/pub28/28apc_002.htm', headers=headers).text, 'html.parser')
    abbv = abbv.find("table", {"id": "ep533076"})
    abbv = abbv.findAll("a")

    streetsabbv = []

    for address in abbv:
        streetsabbv.append(address.get_text().lower())

    del streetsabbv[0:3]

    return list(filter(lambda x: x != ' ', streetsabbv))


def get_secondary_abbv():
    headers = {
    'User-Agent': '',
    }

    abbv = BeautifulSoup(requests.get('https://pe.usps.com/text/pub28/28apc_003.htm', headers=headers).text, 'html.parser')
    abbv = abbv.find("table", {"id":"ep538257"})
    abbv = abbv.findAll("a")

    addressabbv = []

    for abbreviation in abbv:
        addressabbv.append(abbreviation.get_text().translate(str.maketrans(dict.fromkeys(string.punctuation))).lower())

    del addressabbv[52:54]
    del addressabbv[6:8]
    del addressabbv[0:2]

    return addressabbv


def grab_site_address(link, addr, streets):
    data = BeautifulSoup(requests.get(link).text, 'html.parser').prettify().split('\n')
    data = map(lambda x: x.strip(' '),data)
    data = list(filter(lambda x: len(x) > 0, data))
    data = list(filter(lambda x: x[0] not in '!"#$%&\')*+-/:;<=>?@[\\]^_`{|}~', data))

    addresses_mined = 0
    address = []
    found = False

    for index in range(len(data)):
        search=re.search(r"(\s\d{4}\d[-\.\s]??\d{3}\d\b|\s\d{4}\d\b)", data[index])

        if search and not found:
            if re.search(r"([\s]??ga\b)",data[index].lower()) or re.search(r"([\s]??georgia\b)", data[index].lower()):
                tempaddr = [str(data[index])]
                found = True
                count = 0
                while count < 5:  # Safeguard against infinite loop
                    count += 1

                    if any(re.search(rf"[\s]??{address}\b", data[index - count].lower()) for address in addr):
                        tempaddr = [data[index - count]] + tempaddr
                    elif any(re.search(rf"[\s]??{street}\b", data[index - count].lower()) for street in streets):  # This is imperfect due to st being so common.
                        tempaddr = [data[index - count]] + tempaddr
                        break

                possible_address = re.search(r"([\s]??\d{1,6}\s.*\s\d{5}\b|[\s]??\d{1,6}\s.*\s\d{9}\b)",', '.join(tempaddr))
                if possible_address:
                    address.append({'address': possible_address.group(0).strip(' ')})
                else:
                    found = False

        search = re.search(r"([^A-Za-z\d\.]1??[-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}\b|\b1??[-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}\b|[^A-Za-z\d\.]1??[-\.\s]??\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b|\b1??[-\.\s]??\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b|[^A-Za-z\d\.]\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b|\b\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b)", data[index])

        if search and found:
            address[addresses_mined]['phone'] = search.group(0)
            addresses_mined += 1
            found = 0

    return address


if __name__ == '__main__':
    streets = get_street_abbv()
    addr = get_secondary_abbv()

    print(grab_site_address('http://www.gsu.edu', addr, streets))
