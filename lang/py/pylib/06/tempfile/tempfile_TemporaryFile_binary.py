#!/usr/bin/env python

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write('Some data')
    temp.seek(0)
    
    print temp.read()
