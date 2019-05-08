#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class DicHandler(BaseHTTPRequestHandler):

    def __init__(self,thedic,*args,**kwargs):
        self.thedic = thedic      #1.NOOOT 
        BaseHTTPRequestHandler.__init__(self,*args,**kwargs)
    
    def do_GET(self):
        key = self.path[1:]
        if not key in self.thedic:
            self.send_error(404,'NO such Key')
        else:
            self.send_response(200)
            self.send_header('content-type','text/plain')
            self.end_headers()
            resp = "Key :%s\n"%key
            resp += "Value  :%s\n"%self.thedic[key]
            self.wfile.write(resp.encode('latin-1'))
            
d = {
    'name':'Dave',
    'value':[1,2,3,4,5],
    'email':'dave@yahoo.com'
    }

from functools import partial       
serv = HTTPServer(('',9000),partial(DicHandler,d))   #2NOOOOT

from threading import Thread
d_mon = Thread(target=serv.serve_forever)
d_mon.start()

        
