import requests
from bs4 import BeautifulSoup

def get_street_abbv():
    headers = {
    'User-Agent': '',
    }

    abbv = BeautifulSoup(requests.get('https://pe.usps.com/text/pub28/28apc_002.htm',headers=headers).text, 'html.parser')
    abbv = abbv.find("table",{"id": "ep533076"})
    abbv = abbv.findAll("a")

    streetsabbv = []

    for i in abbv:
        streetsabbv.append(i.get_text().lower())

    del streetsabbv[0:3]

    return list(filter(lambda x: x != ' ', streetsabbv))

if __name__ == "__main__":
    abbv = get_street_abbv()
    print(abbv)