import convertapi
import os
import sys

convertapi.api_secret = 'Your-convertapi-apikey'

if len(sys.argv) < 2:
    print ('\n')
    print ("enup filename not passed as 1st Parameter OR Argument")
    print ('\n')
    sys.exit()

filename = sys.argv[1]
pdfn = filename.replace('epub','pdf')
convpdf = convertapi.convert('pdf',{'File': filename})
# save to file to pdf
convpdf.file.save(pdfn)
