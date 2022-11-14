"""
Georgia Institute of Technology - CS1301
HW03 - Loops and Iteration
"""

#########################################

"""
Function Name: userReplace()
Parameters: startingString (str), username (str)
Returns: replacedString (string)
"""
def userReplace(startingString, username):
    replacedString = ""
    for char in startingString:
        if char == "$":
            replacedString = replacedString + username
        else:
            replacedString = replacedString + char
    return replacedString

#########################################

"""
Function Name: specialChar()
Parameters: characterString (str)
Returns: sumOfIndices (int)
"""
def specialChar(characterString):
    sumOfIndices = 0
    index = 0
    for char in characterString:
        if char in "!@#$%^&*":
            sumOfIndices = sumOfIndices + index
        index = index + 1
    return sumOfIndices

#########################################

"""
Function Name: footballGame()
Parameters: score1 (str), score2 (str), team1 (str), team2 (str)
Returns: winningTeam (string)
"""
def footballGame(score1, score2, team1, team2):
    points1 = 0
    points2 = 0
    
    for char in score1:
        if char in "1234567890":
            points1 = points1 + int(char)

    for char in score2:
        if char in "1234567890":
            points2 = points2 + int(char)

    if points1 > points2:
        output = team1
    elif points1 < points2:
        output = team2
    else:
        output = "It's a tie!"

    return output

#########################################

"""
Function Name: buyTheDip()
Parameters: currentPrice (float), finalPrice (float), growth (float)
Returns: days (int)
"""
def buyTheDip(currentPrice, finalPrice, growth):
    days = 0

    while currentPrice > finalPrice:
        currentPrice = currentPrice * (1 + growth * 0.01)
        days = days + 1

    return days

#########################################

"""
Function Name: questionMaker()
Parameters: questions (str), subQuestions (str)
Returns: combinedQuestions (str)
"""
def questionMaker(questions, subQuestions):
    output = ""
    for numbers in questions:
        for letters in subQuestions:
            output = output + numbers + letters

    return output

