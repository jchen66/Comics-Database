#!/usr/bin/python
import csv
import re
import sys


allArtists=[]
def deleteParenthesis(strField):
    tmpStr=strField
    hasP=re.search(r'[ ]*[(][\w ]*[\?|\#|\.|\w|\[|\]|;|\-|\'|"|:|?|! ]*[\w \.]*[)]',tmpStr)
    while hasP:
        tmpStr=re.sub(r'[ ]*[(][\w ]*[\?|\#|\.|\w|\[|\]|;|\-|\'|"|:|?|! ]*[\w \.]*[)]',"",tmpStr)
        hasP=re.search(r'[ ]*[(][\w ]*[\?|\#|\.|\w|\[|\]|;|\-|\'|"|:|?|! ]*[\w \.]*[)]',tmpStr)
    return tmpStr

#check if there is a ';' inbetween brackets
#returns True if it has nested 
def isNested(strField):
    tmpStr=strField
    openBracket=0;
    #parse through every character in a string
    for c in tmpStr:
        if c=='[':
            openBracket+=1
        elif c==']':
            openBracket-=1
        elif c==';':
            if ((openBracket%2)!=0):
                return True

    return False


def matchB(strField):
    tmpStr=strField
    openBracket=0
    start=0
    finish=0
    counter=0
    for c in tmpStr:
        #print(c)
        if c=='[':
            #print("found '[' ")
            if openBracket==0:
                start=counter
            openBracket+=1

        elif c==']':
            openBracket-=1
            if openBracket==0:
                finish=counter
                #print("found finish")
                return [start, finish]
        counter +=1
    return [start, finish]


def findNestedCharacters(strField):
    counter=0
    characters=[]
    tmpStr=deleteParenthesis(strField)
    
    while tmpStr!="":
        #print("tmpStr: "+tmpStr)
        indexC=tmpStr.find(";")
        indexes=matchB(tmpStr)
        indexB=indexes[0]
        indexB2=indexes[1]
        #print("    "+str(indexB))
        #print("    "+str(indexB2))
        #indexB=tmpStr.find("[")
        #indexB2=tmpStr.find("]")

        #simplest case
        #asdas; asdasd[]
        if indexB==0 and indexB2==0:
            tmp=tmpStr.split(';',1)
            try: 
                characters.append(tmp[0])
                tmpStr=""
            except IndexError:
                tmpStr=""

        elif indexC<indexB:
            tmp=tmpStr.split(';',1)

            try:
                tmpStr=tmp[1]
                characters.append(tmp[0].strip())
            except IndexError:
                tmpStr=""
            
        #asdas[simple]; asdasd[dasd; asdasd']
        elif indexC>indexB and indexC>indexB2:
            tmp=tmpStr.split(';',1)
            try:
                tmpStr=tmp[1]
                characters.append(getNickname(tmp[0]))
            except IndexError:
                tmpStr=""


        #asda[dsasd; sdasd[gdfgdf];asdas];hk
        else:
            #print("here")
            Bindexes=matchB(tmpStr)
            #print(Bindexes)
            mainName=tmpStr[:Bindexes[0]].strip()
            associateNames=tmpStr[Bindexes[0]+1:Bindexes[1]]
            restOfStr=tmpStr[Bindexes[1]+1:].strip()
            #print("mainName:"+mainName)
            #print("associateNames: "+associateNames)
            #check if empty or has another ';'
            #tmp2=tmpStr[Bindexes[1]+1:].strip()
            if restOfStr=="":
                tmpStr=""
            else:
                tmp=restOfStr.split(';',1)
                try:
                    #print("p: "+ tmpStr[0])
                    #print(tmp)
                    tmpStr=tmp[1]
                except IndexError:
                    tmpStr=""
            characters.append([mainName, findNestedCharacters(associateNames)])
        #print(characters)


    return characters


#asdas[kjsdfdf]
def getNickname(strField):
    tmpStr=strField
    names=[]
    names.append(tmpStr[0:tmpStr.find("[")].strip())
    names.append(tmpStr[tmpStr.find("[")+1: tmpStr.find("]")].strip())
    return names

#doesn't take in consideration nested brackets
def splitCharacters(strField):
    tmpStr=strField
    characters=tmpStr.split(';')
    for c in characters:
        c=c.strip()
    return characters



# name[nickname]; 
# asda; asdwe[dasd]; 
# asdas[asda;asd;asdas]
def findAllCharacters(strField):
    tmpStr=deleteParenthesis(strField)
    characters=[]
    counter=0;

    hasMany=re.search(r'[;]',tmpStr)
    if hasMany:
        #check if it is nested
        isN=isNested(tmpStr)
        if isN:

            #assume max ONE nested characters
            #print("problem with:"+tmpStr)
            characters.append(findNestedCharacters(tmpStr))
            return characters
        else:
            #split using ';' and for each piece of string--> do the simplest case
            tmpCharacters=splitCharacters(tmpStr)
            #check for nicknames
            for c in tmpCharacters:
                hasB=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|;| ]*[\w \.]*[\]]',c)
                tmpName=c
                if hasB:
                    tmpName=getNickname(c)
                    #notice: can be a list
                characters.append(tmpName)
            return characters



    #simplest case: only one character... maybe has a nickname?
    else:
        #check if has a nickname(aka check for "[]")
        hasB=re.search(r'[\?]*[ ]*[\[][\w ]*[\?|\#|\.|\w|;| ]*[\w \.]*[\]]',tmpStr)
        names=tmpStr
        if hasB:
            names=getNickname(tmpStr)
        characters.append(names)
        return characters

def stripQMark(inputStr):
    tmpStr=re.sub(r'[\?]',"",inputStr)
    return tmpStr.strip()

#####################################################
with open('artists.csv','r', encoding='utf8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print("find artists: "+str(row[0]))
        tmpChar=[]
        try:
            tmp=row[1]
            if tmp=="":
                continue
            tmpChar=findNestedCharacters(tmp)
            for c in tmpChar:

                allArtists.append(c)
        except IndexError:
            continue

    '''
    with open('characters.csv','a') as outcsv:
        f=csv.writer(open('characters.csv','w',newline=''))
        for c in allCharacters:
            f.writerow([c])
    '''
 
    #configure writer to write standard csv file
    writer=csv.writer(open('final_artists.csv','w',newline='', encoding='utf8'))
    writer.writerow(['id','name', 'nickname'])
    id_counter=1
    for artist in allArtists:
        #some may be a list or just string
        print("sort : "+str(id_counter))
        print(artist)
        tmpRow=[]
        nicknameCounter=0
        if len(artist)==0:
            continue
        elif type(artist)==str:
            writer.writerow([id_counter, nicknameCounter, stripQMark(artist),""])
        elif len(artist)==1:
            writer.writerow([id_counter, nicknameCounter, stripQMark(artist[0]),""])
        elif len(artist)==2 and type(artist[1])==str:
            writer.writerow([id_counter, nicknameCounter, stripQMark(artist[0]),artist[1]])
        else:
            n=artist[0] #should be a string
            associates=artist[1] #list ... can be nested too 
            nicknameCounter=1
            for a in associates:
                if type(a)==list:
                    writer.writerow([id_counter, nicknameCounter, stripQMark(n), a[0]])
                else:
                    writer.writerow([id_counter, nicknameCounter, stripQMark(n), a])
                nicknameCounter+=1
        id_counter+=1



