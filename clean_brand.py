#!/usr/bin/python
import csv
import re
import sys


with open('brand_group.csv','r',encoding="utf-8") as origFile:
        reader=csv.reader(origFile)
        f=csv.writer(open('final_brand.csv','w',newline=''))
        numFields=7
        num=0

        for row in reader:
                #match for non ascii numbers
                print(row)
                nameObj= re.match(r'[^\x00-\x7f]', row[1])
                notesObj=re.match(r'[^\x00-\x7f]', row[4])
                urlObj=re.match(r'[^\x00-\x7f]', row[5])

                #if name has weird char--> delete from the csv file (aka don't do anything)
                #if notes has weird char--> delete only that column
                #if url has weird char--> delete only that column
                #else--> cpy to a another file
                if nameObj:
                        #do nothing
                        num=num+1
                else:
                    if notesObj:
                       row[4]=None
                    if urlObj:
                        row[5]=None
                    try: 
                        f.writerow(row)
                    except UnicodeEncodeError:
                        print('not encodable')





