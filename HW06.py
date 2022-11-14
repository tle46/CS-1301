"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
"""

#########################################

"""
Function Name: possibleMovies()
Parameters: movies(dict), time (str)
Returns: list of movie names (list)
"""
def possibleMovies(movies, availTime):
    movieList = []
    for movie in movies:
        for time in movies[movie]:
            if time == availTime:
                movieList.append(movie)
    movieList.sort()
    return movieList

#########################################

"""
Function Name: gameSelector()
Parameters: gameList (list), filterType (str)
Returns: dictionary of games mapped to a boolean value (dict)
"""
def gameSelector(gameList, filterType):
    gameDict = {}
    for game in gameList:
        if game == "":
            gameDict[game] = False
        elif filterType == "even":
            gameDict[game] = (len(game) % 2 == 0)
        elif filterType == "odd":
            gameDict[game] = (len(game) % 2 == 1)
    return gameDict

    
#########################################

"""
Function Name: foodDecoder()
Parameters: secretList1 (list), secretList2 (list)
Returns: list of combined strings and the number of errors (list)
"""
def foodDecoder(secretList1, secretList2):
    outputList = []
    errorCount = 0
    for i in range(len(secretList1)):
        try:
            outputList.append(secretList1[i] + secretList2[i])
        except:
            errorCount += 1
    outputList.append(errorCount)
    return outputList

#########################################

"""
Function Name: cheapestLocations()
Parameters: activities (dict)
Returns: dictionary mapping each activity to a location (dict)
"""
def cheapestLocations(activityDict):
    cheapestDict = {}
    for activity in activityDict:
        minCost = 9999999999
        for location in activityDict[activity]:
            if activityDict[activity][location] < minCost:
                cheapestDict[activity] = location
                minCost = activityDict[activity][location]
    return cheapestDict

#########################################

"""
Function Name: sportSuggestions()
Parameters: friends mapped to their suggested sports (dict)
Returns: dictionary mapping each sport to the list of friends who selected these sports (dict).
"""
def sportSuggestions(nameSportDict):
    sportNameDict = {}
    for name in nameSportDict:
        for sport in nameSportDict[name]:
            if sport in sportNameDict:
                sportNameDict[sport].append(name)
                sportNameDict[sport].sort()
            else:
                sportNameDict[sport] = [name]
    return sportNameDict



