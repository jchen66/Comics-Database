//////////////// Code for splitting characters

import csv

genres = set()

with open('story.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        try:
            g = row[11]
            if g:
                #g_split contains all the uncleaned character names separated by ';'
                g_split = g.split(';')
                for item in g_split:
                    item = item.strip()
                    item = item.title()
                    if(item.isdigit() == False and item != '?'):
                        genres.add(item)
        except IndexError:
            pass
    genres = list(genres)

ct = 1
genreCSV = []
for genre in genres:
    if genre:
        genreCSV.append([ct,genre])
        ct=ct+1

with open('genre.csv', 'a') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['id', 'name'])
    for item in genreCSV:
        #Write item to outcsv
        writer.writerow([item[0], item[1]])


"""
Pseudocode:

For each string in the array:
    Find the first '{'. If there is none, leave that string alone.
    Init a counter to 0. 
    For each character in the string:  
        If you see a '{', increment the counter.
        If you see a '}', decrement the counter.
        If the counter reaches 0, break.
    Here, if your counter is not 0, you have invalid input (unbalanced brackets)
    If it is, then take the string from the first '{' up to the '}' that put the
     counter at 0, and that is a new element in your array.
"""
def matchBracets(str):





