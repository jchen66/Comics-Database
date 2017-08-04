#!/usr/bin/python
import csv

with open('/Users/Yutong/Desktop/assignments/EPFL4A/Database/Project/comics/publisher.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    num = 0

    # year_began, year_ended
       
    digit_cols = [3,4]
    ct=0


    for row in readCSV:
        
        for num in digit_cols:
            if row[num].isdigit()==False or len(row[num])!=4:
                row[num]=None
            elif row[num] and row[num].isdigit()==True:
                try:
                    value=int(row[num])
                    if value > 2020:
                        row[num]=None
                    if value < 1800:
                        row[num]=None
                except TypeError:
                    pass
            ct=ct+1

