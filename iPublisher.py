#!/usr/bin/python
import csv
import re
import sys

#indicia publisher has 9 fields
with open('indicia_publisher.csv','r',encoding="utf-8") as origFile:
	reader=csv.reader(origFile)
	f=csv.writer(open('final_indicia_publisher.csv','w',newline=''))
	numFields=9
	num=0
	maxName=0;   #124
	maxNotes=0;  #2593
	maxUrl=0;    #115

	for row in reader:
		#match for non ascii numbers
		print(row)
		nameObj= re.match(r'[^\x00-\x7f]', row[1])
		notesObj=re.match(r'[^\x00-\x7f]', row[7])
		urlObj=re.match(r'[^\x00-\x7f]', row[8])
		y_began=re.match(r'NULL',row[4])
		y_ended=re.match(r'NULL',row[5])

		#if name has weird char--> delete from the csv file (aka don't do anything)
		#if notes has weird char--> delete only that column
		#if url has weird char--> delete only that column
		#else--> cpy to a another file
		if nameObj:
			#do nothing
			num=num+1
		else:
			if len(row[1])>maxName:
				maxName=len(row[1])
			if len(row[7])>maxNotes:
				maxNotes=len(row[7])
			if len(row[8])>maxUrl:
				maxUrl=len(row[8])

			if notesObj:
				row[7]=None
			if urlObj:
				row[8]=None
			if y_began:
				row[4]=None
			if y_ended:
				row[5]=None
			#f.writerow(row)
			try:
				f.writerow(row)
			except UnicodeEncodeError:
				print('not encodable')
	print(maxName)
	print(maxNotes)
	print(maxUrl)
