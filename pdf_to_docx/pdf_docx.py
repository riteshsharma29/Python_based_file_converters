import convertapi
import os
import sys

convertapi.api_secret = 'Your-convertapi-apikey'

if len(sys.argv) < 2:
    print ('\n')
    print ("PDF filename not passed as 1st Parameter OR Argument")
    print ('\n')
    sys.exit()

filename = sys.argv[1]
docf = filename.replace('pdf','docx')
convdocx = convertapi.convert('docx',{'File': filename})
# save to file to pdf
convdocx.file.save(docf)
