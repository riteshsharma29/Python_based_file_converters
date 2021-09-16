import convertapi
import os
import sys

convertapi.api_secret = 'oQgN1dXVk3ce0NIP'

if len(sys.argv) < 2:
    print ('\n')
    print ("docx filename not passed as 1st Parameter OR Argument")
    print ('\n')
    sys.exit()

filename = sys.argv[1]
docf = filename.replace('docx','pdf')
convdoc = convertapi.convert('pdf',{'File': filename})
# save to file to docx
convdoc.file.save(docf)
