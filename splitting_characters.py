import csv

characters = set()

with open('final_story.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        try:
            a = row[11]
            if a:
                a_split = a.split(';')
                for item in a_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        characters.add(item)
        except IndexError:
            pass
    characters = list(characters)

    for row in readCSV:
        try:
            b = row[2]
            if b:
                b_split = b.split(';')
                for item in b_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        characters.add(item)
        except IndexError:
            pass
    characters = list(characters)

ct = 1
charactersCSV = []
for characters in characters:
    if characters:
        charactersCSV.append([ct,characters])
        ct=ct+1

with open('characters.csv', 'a') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['id', 'name'])
    for item in charactersCSV:
        #Write item to outcsv
        writer.writerow([item[0], item[1]])
