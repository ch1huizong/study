#!/usr/bin/env python
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib
import urllib2

class MultiPartForm(object):
    
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
        
    def get_content_type(self):
        return 'multipart/form-data;boundary=%s'%self.boundary

    def add_field(self,name,value):
        self.form_fields.append((name,value))
        return

    def add_file(self, fieldname, filename, fileHandle,mimetype=None):
        """Add a file to be uploaded"""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = (mimetypes.guess_type(filename)[0] or
                        'application/octet-stream')
        self.files.append((fieldname, filename, mimetype,body))
        return

    def __str__(self):
        """Return a string representing the form data,including the attached
            files.
        """
        
        parts = []
        part_boundary = '--'+self.boundary

        parts.extend(
            [ part_boundary,
             'Content-Dispositon:form-data;name="%s"'%name,'',
             value,
            ]
            for name, value in self.form_fields
            )

        #Add files to upload
        parts.extend([
            part_boundary,
            'Content-Disposition:file; name="%s";filename="%s"'%\
            (field_name, filename),
            'Content-Type:%s'%content_type,
            '',
            body,
            ] 
            for field_name, filename, content_type,body in self.files
            )
        #Flatten the list 
        flattened =  list(itertools.chain(*parts))
        flattened.append('--'+self.boundary+'--')
        flattened.append('')
        return '\r\n'.join(flattened)



if __name__ == '__main__':
    #Create the form with simple fields
    form = MultiPartForm()
    form.add_field('firstname','Doug')
    form.add_field('lastname','Hellmann')

    #add a fake file
    form.add_file('biography','bio.txt',
                    fileHandle = StringIO('python developer and blogger.'))

    #build the request
    request = urllib2.Request('http://localhost:8080/')
    request.add_header(
        'User-agent',
        'PyMOTW')
    body = str(form)
    request.add_header('Content-Type',form.get_content_type())
    request.add_header('Content-Length',len(body))
    request.add_data(body)

    print
    print'OUTGOING DATA:'
    print request.get_data()

    print
    print'Server Response:'
    print urllib2.urlopen(request).read()
