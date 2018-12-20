#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi 

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        #parse the form data posted
        form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],})
        
        #Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client:%s\n'%str(self.client_address))
        self.wfile.write('User-agent:%s\n'%str(self.headers['user-agent']))
        self.wfile.write('Path:%s\n'%self.path)
        self.wfile.write('Form data:\n')

        #Echo back posted information
        for field in form.keys():
            field_item = form[field]

            if field_item.filename:
                
                 #it's a file
                 # Note: We can add functions to deal with files

                # with open('post1.txt','w') as f:
                file_data = field_item.file.read()
                #     f.write(file_data)
                    
                file_len = len(file_data)
                del file_data
                self.wfile.write(
                    '\tUploaded %s as "%s" (%d bytes)\n'%\
                    (field,field_item.filename,file_len))
            else:
                self.wfile.write('\t%s=%s\n'%(field,form[field].value))
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost',8080),PostHandler)
    print'Starting server,use <CTRL-C> to stop'
    server.serve_forever()
