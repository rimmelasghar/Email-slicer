#Code made by Rimmel Asghar

import re
def Email_slicer(file):
    print(' Welcome to Email Slicer')
    infile=open(file,'rt')
    newfile=open('Sliced_emails.txt','w')
    content=infile.read()
    infile.close()
    bag=content.split('\n')
    for i in bag:
        x=re.split('@',i)
        newfile.write('Name : {}\t\t\t| Domain : {}\n'.format(x[0],x[1]))
    newfile.close()
    print('A new file "Sliced_emails.txt" has been made in the default folder.')


Email_slicer('email.txt')