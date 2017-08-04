#!/usr/bin/python
import csv
import re
import sys

#indicia publisher has 9 fields
with open('story.csv','r',encoding="utf-8") as origFile:
	reader=csv.reader(origFile)
	f=csv.writer(open('final_story.csv','w',newline=''))
	numFields=1
	num=0
	maxtitle=0    #239
	maxfeature=0  #200
	maxscript=0   #3868
	maxpencils=0   #200
	maxinks=0     #709
	maxcolors=0   #140
	maxletters=0 #90
	maxediting=0 #93
	maxgenre=0   #19
	maxchar=0
	maxsynopsis=0
	maxreprint=0
	maxnotes=0

	for row in reader:
		#match for non ascii numbers
		print(row[0])
		title= re.match(r'[^\x00-\x7f]', row[1])
		feature=re.match(r'[^\x00-\x7f]', row[2])

		#check for ? marks
		script=re.match(r'[^\x00-\x7f]', row[4])
		q_script=re.search(r'[\?]+$', row[4])
		b_script=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]', row[4])

		pencils=re.match(r'[^\x00-\x7f]', row[5])
		q_pencils=re.search(r'[\?]+$',row[5])
		b_pencils=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]', row[5])

		inks=re.match(r'[^\x00-\x7f]', row[6])
		q_inks=re.search(r'[\?]+$',row[6])
		b_inks=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]', row[6])

		colors=re.match(r'[^\x00-\x7f]', row[7])
		q_colors=re.search(r'[\?]+$', row[7])
		b_colors=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]', row[7])

		letters=re.match(r'[^\x00-\x7f]', row[8])
		q_letters=re.search(r'[\?]+$', row[8])
		b_letters=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]', row[8])

		editing=re.match(r'[^\x00-\x7f]', row[9])
		genre=re.match(r'[^\x00-\x7f]', row[10])
		characters=re.match(r'[^\x00-\x7f]', row[11])
		synopsis=re.match(r'[^\x00-\x7f]', row[12])
		reprint=re.match(r'[^\x00-\x7f]', row[13])
		notes=re.match(r'[^\x00-\x7f]', row[14])

		#if name has weird char--> delete from the csv file (aka don't do anything)
		#if notes has weird char--> delete only that column
		#if url has weird char--> delete only that column
		#else--> cpy to a another file
		if title:
			#do nothing
			num=num+1
		else:
			if len(row[1])>maxtitle:
				maxtitle=len(row[1])
			if len(row[2])>maxfeature:
				maxfeature=len(row[2])
			if len(row[4])>maxscript:
				maxscript=len(row[4])
			if len(row[5])>maxpencils:
				maxColor=len(row[5])
			if len(row[6])>maxinks:
				maxDim=len(row[6])
			if len(row[7])>maxcolors:
				maxPaper=len(row[7])
			if len(row[8])>maxletters:
				maxletters=len(row[8])
			if len(row[9])>maxediting:
				maxediting=len(row[9])
			if len(row[10])>maxgenre:
				maxgenre=len(row[10])
			if len(row[11])>maxchar:
				maxchar=len(row[11])
			if len(row[12])>maxsynopsis:
				maxsynopsis=len(row[12])
			if len(row[13])>maxreprint:
				maxreprint=len(row[13])
			if len(row[14])>maxreprint:
				maxreprint=len(row[14])

			



			if feature:
				row[2]=None
			if script:
				row[4]=None
			if q_script:
				try:
					tmpscript=row[4]
					row[4]=tmpscript[:-1]
				except TypeError:
					#do nothing
					row[4]=row[4]

			#if there are brackets in the data
			if b_script:
				try:
					tScript=re.sub(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]',"",row[4])
					row[4]=tScript
				except TypeError:
					row[4]=row[4]

			if pencils:
				row[5]=None
			if q_pencils:
				try: 
					tmppencils=row[5]
					row[5]=tmppencils[:-1]
				except TypeError:
					#do nothing
					row[5]=row[5]

			if b_pencils:
				try: 
					tPencils=re.sub(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]',"",row[5])
					row[5]=tPencils
				except TypeError:
					row[5]=row[5]

			if inks:
				row[6]=None
			if q_inks:
				try:
					tmpinks=row[6]
					row[6]=tmpinks[:-1]
				except TypeError:
					#donothing
					row[6]=row[6]

			if b_inks:
				try: 
					tInks=re.sub(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]',"",row[6])
					row[6]=tInks
				except TypeError:
					row[6]=row[6]

			if colors:
				row[7]=None
			if q_colors:
				try:
					tmpcolors=row[7]
					row[7]=tmpcolors[:-1]
				except TypeError:
					#donothing
					row[7]=row[7]

			if b_colors:
				try: 
					tColors=re.sub(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]',"",row[7])
					row[7]=tColors
				except TypeError:
					row[7]=row[7]

			if letters:
				row[8]=None
			if q_letters:
				try:
					tmpletters=row[8]
					row[8]=tmpletters[:-1]
				except TypeError:
					#donothing
					row[8]=row[8]

			if b_letters:
				try:
					tLetters=re.sub(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|\'| ]*[\w \.]*[\]]',"",row[8])
					row[8]=tLetters
				except TypeError:
					row[8]=row[8]



			if editing:
				row[9]=None
			if genre:
				row[10]=None
			if characters:
				row[11]=None
			if synopsis:
				row[12]=None
			if reprint:
				row[13]=None
			if notes:
				row[14]=None


			
			#f.writerow(row)
			try:
				f.writerow(row)
			except UnicodeEncodeError:
				print('not encodable')
	print(maxtitle)   #19727
	print(maxfeature)  #423
	print(maxscript)   #1166
	print(maxpencils)  #0
	print(maxinks)     #0
	print(maxcolors)   #0
	print(maxletters)  #267
	print(maxediting)  #347
	print(maxgenre)    #80
	print(maxchar)     #3675
	print(maxsynopsis) #17655
	print(maxreprint)  #5515
	print(maxnotes)    #0



#?[blablabla]
#take out question mark and info in brackets --->  
#RE:    [(\[][A-z ]*[)\]]$

#[asdas?asdasd]
#RE: [(\[][A-z ]*\?*[A-z ]*[)\]]$