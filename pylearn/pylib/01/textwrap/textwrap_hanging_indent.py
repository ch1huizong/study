#!/usr/bin/env python

import textwrap
from example import sample

de_text = textwrap.dedent(sample).strip()
print textwrap.fill(de_text,
                    initial_indent='',
                    subsequent_indent='*'*4,
                    width=50,
                    )

