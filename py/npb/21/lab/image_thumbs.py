#! /usr/bin/env python
# -*- coding:UTF -*-

import os
import time

from multiprocessing import Pool
from PIL import Image

SIZE = (75, 75)
SAVE_DIR = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder) 
            if 'jpg' in f or 'jpeg' in f
            )

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIR, fname)
    im.save(save_path)

if __name__ == '__main__':
    folder = '/root/self/start/beauty'
    os.mkdir(os.path.join(folder,SAVE_DIR))
    images = get_image_paths(folder)

#    start_time = time.time()
#    for image in images:
#        create_thumbnail(image)
#    print "Time :",time.time() - start_time


    start_time = time.time()
    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()
    print "Time :",time.time() - start_time

