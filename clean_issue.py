#!/usr/bin/python
import csv
import re
import sys



with open('issue.csv','r',encoding="utf-8") as origFile:
        reader=csv.reader(origFile)
        f=csv.writer(open('final_issue.csv','w',newline=''))
        numFields=16
        num=0
        
        # series_id, indicia_publisher_id, page_count, valid_isbn, barcode
        digit_cols = [2,3,6,11,12]
        # indicia_frequency, editing, notes, title, rating
        char_cols = [7,8,9,13,15,4,14]
        # publication_date, on_sale_date
        date_cols = [4,14]
        
        for row in reader:
                #match for non ascii numbers
                print(row)

                for num in digit_cols:
                    if row[num].isdigit()==False:
                        row[num]=None
                           
                for num in char_cols:
                    obj = re.match(r'[^\x00-\x7f]', row[num])
                    if obj or obj=='?':
                        row[num]=None
                try: 
                    f.writerow(row)
                except UnicodeEncodeError:
                        print('not encodable')






