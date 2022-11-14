"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

#########################################

"""
Function Name: add()
Parameters: list of ints (list)
Returns: total (int)
"""
def add(numList):
    if len(numList) == 0:
        output = 0
    else:
        output = numList[0] + add(numList[1:])
    return output

#########################################

"""
Function Name: decoder()
Parameters: encryption (str)
Returns: codeword (str)
"""
def decoder(strIn):
    if len(strIn) == 0:
        output = ""
    else:
        if strIn[0].isalpha():
            output = strIn[0] + decoder(strIn[1:])
        else:
            output = decoder(strIn[1:])
    return output

    
#########################################

"""
Function Name: pirateTreasure()
Parameters: directions (list)
Returns: distance_to_treasure (int)
"""
def pirateTreasure(directionList):
    if len(directionList) == 0:
        output = 0
    else:
        if directionList[0] == "up":
            output = 1 + pirateTreasure(directionList[1:])
        else:
            output = -1 + pirateTreasure(directionList[1:])
    return output

#########################################

"""
Function Name: lengthDict()
Parameters: list of names (list)
Returns: dictionary mapping names to length (dict)
"""
def lengthDict(nameList):
    if len(nameList) == 0:
        output = {}
    else:
        counter = 0
        for char in nameList[0]:
            if char.lower() in "bcdfghjklmnpqrstvwxyz":
                counter += 1
        interDict = lengthDict(nameList[1:])
        interDict[nameList[0]] = counter
        output = interDict
    return output

#########################################

"""
Function Name: balancedStr()
Parameters: string of characters (str)
Returns: isBalanced (bool)
"""
def balancedStr(strInput):
    if len(strInput) < 2:
        output = True
    else:
        if strInput[0].isupper() == strInput[-1].isupper():
            output = True
        else:
            output = False
        output = output and balancedStr(strInput[1:-1])
    return output



