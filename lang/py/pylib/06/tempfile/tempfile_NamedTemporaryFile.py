#!/usr/bin/env python

import os
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print'temp:'
    print'  ',temp
    print'temp.name:'
    print'  ',temp.name

print'Exists after close:',os.path.exists(temp.name)
