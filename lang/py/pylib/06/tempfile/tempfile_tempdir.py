#!/usr/bin/env python

import tempfile

tempfile.tempdir='/I/changed/this/path'
print'gettempdir():',tempfile.gettempdir()
