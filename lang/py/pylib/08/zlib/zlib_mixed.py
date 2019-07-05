#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 以decompressobj混合解压

import zlib
import binascii

lorem = open('lorem.txt','rt').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

# 压缩的解压,没压缩的不管
decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

match = decompressed == lorem
print 'Decompressed matches lorem:',match
unused_matches = decompressor.unused_data == lorem
print 'Unused data matches lorem :',unused_matches







