# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import operator

from django.shortcuts import render

from nginxlog import nginx_log

LOG_DIR = '/var/log/nginx'

def list_files(request):
    file_list = [ 
        f for f in os.listdir(LOG_DIR) 
        if os.path.isfile(os.path.join(LOG_DIR, f))
    ]
    return render(request, 'logview/list_files.html', {'file_list': file_list})

def view_log(request, sortmethod, filename):
    logfile = open(os.path.join(LOG_DIR, filename), 'r')
    loglines = list(nginx_log(logfile))
    logfile.close()
    
    try:
        loglines.sort(key=operator.itemgetter(sortmethod))
    except KeyError:
        pass
    return render(
        request, 
        'logview/view_logfile.html', 
        {
            'loglines': loglines, 
            'filename': filename
        }
    )
