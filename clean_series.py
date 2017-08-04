#!/usr/bin/python
import csv
import re
import sys

#indicia publisher has 9 fields
with open('series.csv','r',encoding="utf-8") as origFile:
	reader=csv.reader(origFile)
	f=csv.writer(open('final_series.csv','w',newline=''))
	numFields=1
	num=0
	maxName=0    #239
	maxFormat=0  #200
	maxNotes=0   #3868
	maxColor=0   #200
	maxDim=0     #709
	maxPaper=0   #140
	maxBinding=0 #90
	maxPFormat=0 #93
	maxPType=0   #19

	for row in reader:
		#match for non ascii numbers
		print(row)
		nameObj= re.match(r'[^\x00-\x7f]', row[1])
		formatObj=re.match(r'[^\x00-\x7f]', row[2])
		notesObj=re.match(r'[^\x00-\x7f]', row[11])
		colorObj=re.match(r'[^\x00-\x7f]', row[12])
		dimensionsObj=re.match(r'[^\x00-\x7f]', row[13])
		paperObj=re.match(r'[^\x00-\x7f]', row[14])
		bindingObj=re.match(r'[^\x00-\x7f]', row[15])
		pFormatObj=re.match(r'[^\x00-\x7f]', row[16])
		pTypeIDObj=re.match(r'[^\x00-\x7f]', row[17])

		y_began=re.match(r'NULL',row[3])
		y_ended=re.match(r'NULL',row[4])

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
			if len(row[2])>maxFormat:
				maxFormat=len(row[2])
			if len(row[11])>maxNotes:
				maxNotes=len(row[11])
			if len(row[12])>maxColor:
				maxColor=len(row[12])
			if len(row[13])>maxDim:
				maxDim=len(row[13])
			if len(row[14])>maxPaper:
				maxPaper=len(row[14])
			if len(row[15])>maxBinding:
				maxBinding=len(row[15])
			if len(row[16])>maxPFormat:
				maxPFormat=len(row[16])
			if len(row[17])>maxPType:
				maxPType=len(row[17])
			if y_began:
				row[3]=None
			if y_ended:
				row[4]=None





			if formatObj:
				row[2]=None
			if notesObj:
				row[11]=None
			if colorObj:
				row[12]=None
			if dimensionsObj:
				row[13]=None
			if paperObj:
				row[14]=None
			if bindingObj:
				row[15]=None
			if pFormatObj:
				row[16]=None
			if pTypeIDObj:
				row[17]=None
			#f.writerow(row)
			try:
				f.writerow(row)
			except UnicodeEncodeError:
				print('not encodable')
	print(maxName)   #124
	print(maxFormat)  #2593
	print(maxNotes)   #115
	print(maxColor)
	print(maxDim)
	print(maxPaper)
	print(maxBinding)
	print(maxPFormat)
	print(maxPType)


