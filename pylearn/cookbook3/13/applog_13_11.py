#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/05 10:39:56
# @Author  : che
# @Email   : ch1huizong@gmail.com

import logging
import logging.config


def main():
    logging.basicConfig(
        filename='app.log', 
        level=logging.WARNING,
        format='%(levelname)s:%(asctime)s:%(message)s'     
    )

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown', hostname)
    logging.error('Coundnt find %r', item)
    logging.warning('Feature isdeprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()
