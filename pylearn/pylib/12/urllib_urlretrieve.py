#!/usr/bin/env python

import urllib
import os

def reporthook(blocks_read, block_size, total_size):
    if not blocks_read:
        print'Connection opened'
        return

    if total_size < 0:
        print'Read %d blocks (%d bytes)'(blocks_read,blocks_read*block_size)
    else:
        amount_read = blocks_read * block_size
        print'Read %d blocks,or %d/%d'%\
            (blocks_read,amount_read,total_size)
try:
    filename, msg = urllib.urlretrieve(
        'http://blog.doughellmann.com',
        reporthook = reporthook)
    print
    print'File:',filename
    print'Headers:'
    print msg
    print'File exists before cleanup:',os.path.exists(filename)

finally:
    urllib.urlcleanup()
    print'File Still exists:',os.path.exists(filename)

