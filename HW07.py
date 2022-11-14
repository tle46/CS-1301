"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O & CSV
"""

def musicInputToList(fileName):
    musicFile = open(fileName, "r")
    nonCatList = musicFile.readlines()
    tempList = []
    catList = []
    for index in range(len(nonCatList)):
        nonCatList[index] = nonCatList[index].replace("\n","")
        if not (nonCatList[index] == "" or nonCatList[index] == "Music data"):
            tempList.append(nonCatList[index])
    for index in range(0,len(tempList),3):
        catList.append([tempList[index], tempList[index+1], tempList[index+2]])
    musicFile.close()
    return catList

def artistInputToDict(fileName):
    artistFile = open(fileName, "r")
    lineList = artistFile.readlines()
    artistDict = {}
    for i in range(1, len(lineList)):
        lineList[i] = lineList[i].replace("\n","")
        artist, albCreated, albSold, billBoard = lineList[i].split(",")        
        artistDict[artist] = [int(albCreated), int(albSold), int(billBoard)]
    return artistDict
    

#########################################

"""
Function Name: sortByArtist()
Parameters: filename (str), artist (str)
Returns: list of songs (list)
"""
def sortByArtist(fileName, artistSearch):
    musicList = musicInputToList(fileName)
    songList = []
    for name, genre, artist in musicList:
        if artist == artistSearch:
            songList.append(name)
    return songList
        
#########################################

"""
Function Name: genreFilter()
Parameters: filename (str)
Returns: mapping of songs to lists of genres of that song (dict)
"""
def genreFilter(fileName):
    musicList = musicInputToList(fileName)
    genreDict = {}
    for name, genre, artist in musicList:
        genreDict[genre] = []
    for name, genre, artist in musicList:
        genreDict[genre].append(name)
    return genreDict

    
#########################################

"""
Function Name: sortByGenre()
Parameters: filename (str), genre (str), output filename (str)
Returns: None (NoneType)
"""
def sortByGenre(fileName, genreSearch, outFileName):
    genreDict = genreFilter(fileName)
    musicList = musicInputToList(fileName)    
    musicFile = open(outFileName, "w")
    genreSearch = genreSearch.strip()
    if genreSearch in genreDict:
        songList = genreDict[genreSearch]
        songList.sort()
        musicFile.write(genreSearch + "\n")
        for index, song in enumerate(songList):
            musicFile.write("\n" + str(index + 1) + ". " + song + " - " + findArtist(musicList, song))                     
    else:
        musicFile.write(genreSearch + "\n")
    musicFile.close()

def findArtist(musicList, song):
    for index, (name, genre, artist) in enumerate(musicList):
        if name == song:
            return artist

#########################################

"""
Function Name: biggestSuccess()
Parameters: filename (str), artists (list)
Returns: artist and percentage (tuple)
"""
def biggestSuccess(fileName, artistSearchList):
    artistDict = artistInputToDict(fileName)
    highestRatio = 0
    highestArtist = ""
    for artist in artistSearchList:
        if artist in artistDict:
            albCreated, albSold, billBoard = artistDict[artist]
            try:
                if (billBoard/albCreated) > highestRatio:
                    highestRatio = billBoard/albCreated
                    highestArtist = artist
            except:
                continue
    highestRatio = round(highestRatio * 100, 2)
    if highestRatio == 0:
        returnTup = ()
    else:
        returnTup = (highestArtist, highestRatio)
    return returnTup

#########################################

"""
Function Name: grammyAwards()
Parameters: filename (str), artists (list)
Returns: category of artists by celebrity status (dict)
"""
def grammyAwards(fileName, artistSearchList):
    artistDict = artistInputToDict(fileName)
    rankDict = {"A-List": [], "B-List": [], "C-List": []}
    for artist in artistDict:
        if artist in artistSearchList:
            albCreated, albSold, billBoard = artistDict[artist]
            try:
                ratio = billBoard/albCreated
            except:
                continue
            if ratio <= 0.3:
                rankDict["C-List"].append(artist)
            elif ratio <= 0.7:
                rankDict["B-List"].append(artist)
            else:
                rankDict["A-List"].append(artist)
    return rankDict



