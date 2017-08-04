import csv

artists = set()

path = '/Users/Yutong/Dropbox/DB Project/cleaned csv files/final_story.csv'

with open(path,encoding = "ISO-8859-1") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:                                 #script
        try:
            a = row[4]
            if a:
                a_split = a.split(';')
                for item in a_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        artists.add(item)
        except IndexError:
            pass
    artists = list(artists)

    for row in readCSV:                                 #pencils
        try:
            b = row[5]
            if b:
                b_split = b.split(';')
                for item in b_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        artists.add(item)
        except IndexError:
            pass
    artists = list(artists)

    for row in readCSV:                                 #inks
        try:
            b = row[6]
            if b:
                b_split = b.split(';')
                for item in b_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        artists.add(item)
        except IndexError:
            pass
    artists = list(artists)

    for row in readCSV:                                  #colors
        try:
            b = row[7]
            if b:
                b_split = b.split(';')
                for item in b_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        artists.add(item)
        except IndexError:
            pass
    artists = list(artists)

    for row in readCSV:                                    #letters
        try:
            b = row[8]
            if b:
                b_split = b.split(';')
                for item in b_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        artists.add(item)
        except IndexError:
            pass
    artists = list(artists)

ct = 1
artistsCSV = []
for artists in artists:
    if artists:
        artistsCSV.append([ct,artists])
        ct=ct+1

with open('artists.csv', 'a') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['id', 'name'])
    for item in artistsCSV:
        #Write item to outcsv
        writer.writerow([item[0], item[1]])
