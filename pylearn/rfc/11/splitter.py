#!/usr/bin/env python
# -*- coding:UTF -*-

def split(line, types=None,delimiter=None):
    """
        Splite a line of text and optionally performs type conversion.
        By default, splitting is performed on whitespace, but a different
        delimiter can be selected with delimiter keyword argument.
        For example:接下来的才是最重要的!

        >>> split('GOOG 100 490.50')
        ['GOOG', '100', '490.50']

        >>> split('GOOG 100 490.5', [str, int, float])
        ['GOOG', 100, 490.5]

        >>> split('GOOG,100,490.50', delimiter=',')
        ['GOOG', '100', '490.50']


    """
    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty,val in zip(types,fields)]
    return fields

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
