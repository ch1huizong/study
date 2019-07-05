#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import os
from multiprocessing.dummy import Pool
import re

import requests
from bs4 import BeautifulSoup

def download(url):
    image = requests.get(url, stream=True)
    head, filename = os.path.split(url)
    filename = os.path.join('tmp',filename)

    with open(filename,'wb') as f:
        for chunk in image.iter_content(chunk_size=128):
            f.write(chunk)


url = 'http://www.jiemian.com'
html = requests.get(url).text
bs = BeautifulSoup(html,'lxml')

images = (image.get('src') 
            for image in bs.find_all('img',src=re.compile('^http://')))

p = Pool(16)
p.map(download, images)
p.close()
p.join()
