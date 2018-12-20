#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys

def put(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(",")
        name = fields[0]
        shares = int(fields[1])
        price = float(fields[2])
        stock = (name, shares, price)
        portfolio.append(stock)
    return portfolio

def get(records):
    for name, shares, price in records:
        print"Name:",name
        print"Shares:",shares
        print"Price:",price


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print"Please input a filename:"
        raise SystemExit(1)
    records = put(sys.argv[1])
    get(records)
