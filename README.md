# Python_based_file_converters
Python based file converters


1) PDF file to Microsoft docx file
2) csv file to Microsoft excel file 
3) Microsoft docx file to PDF file
4) epub file to PDF file

All dependecncies can be installed using pip :

Make below change once you install convertapi module. Signup to https://www.convertapi.com/ and get your free api key as you will this in your script. If you have bulk usage then recommend you check pricing.  

For example am using Python 3.9
C:\Python39\Lib\site-packages\convertapi
Open __init__.py and change below line 

From

conversion_timeout = None

To

conversion_timeout = 180

and save the file.
