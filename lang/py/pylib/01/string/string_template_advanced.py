#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import string

template_text = """
    Delimiter   :%%
    Replaced    :%with_underscore
    Ignored     :%notunderscored
"""

d = {
    'with_underscore':'Replaced',
    'notunderscored':'not replaced',
}

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate(template_text)

print t.safe_substitute(d)
