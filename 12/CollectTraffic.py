import os
import datetime
import time
import json
import requests
from bs4 import BeautifulSoup
import urllib

location = 'Rhode Island Ave @ 18th St'
dirpath = location.replace('@','at').replace(' ','_')
dirpath = datetime.datetime.now().strftime('%d%m%Y_%H%M_') + dirpath

os.mkdir(dirpath)

images = 5

count = 0
while count < images:
    if count % 500 == 0:
        soup = BeautifulSoup(requests.get('http://app.ddot.dc.gov/').text, 'html.parser')
        imageObj = str(soup.find_all("script")[2])

        imageObj = imageObj[58:-17]
        jsondict = json.loads(imageObj)

        for cameras in jsondict:
            if dict(cameras).get('name') == location:
                image = dict(cameras).get('image').encode('ascii', 'ignore')
                break

    urllib.request.urlretrieve(image.decode('ascii'), os.path.join(dirpath, 'Image' + str(count) + '.jpeg'))
    count += 1

    time.sleep(5)