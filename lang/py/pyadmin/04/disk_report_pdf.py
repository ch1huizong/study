#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 21:13:49
# @Author  : che
# @Email   : ch1huizong@gmail.com

import subprocess
import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def disk_report():
    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()[1:]


def create_pdf(iput, output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11 * inch)
    textobject.textLines(
        """
    Disk Capacity Report: %s
    """
        % date
    )
    for line in iput:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()


report = disk_report()
create_pdf(report)
