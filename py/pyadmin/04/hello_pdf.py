#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 19:59:15
# @Author  : che
# @Email   : ch1huizong@gmail.com

from reportlab.pdfgen import canvas


def hello():
    c = canvas.Canvas("hello.pdf")
    c.drawString(100, 100, "Hello World")
    c.showPage()
    c.save()


hello()
