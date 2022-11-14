"""
Georgia Institute of Technology - CS1301
HW04 - Strings, indexing and lists
"""

#########################################

"""
Function Name: fixTickets()
Parameters: ticketNumber (str)
Returns: fixedTicket (str)
"""
def fixTickets(ticketNumber):
    fixedTicket = ""
    for i in range(len(ticketNumber)):
        if ticketNumber[i] in "0123456789":
            strAdd = ticketNumber[i]
        elif ticketNumber[i].isupper():
            strAdd = ticketNumber[i].lower()
        else:
            strAdd = ticketNumber[i].upper()
        fixedTicket += strAdd
    return fixedTicket

#########################################

"""
Function Name: secret()
Parameters: message (str)
Returns: secret message (str)
"""
def secret(message):
    messageArray = message.split()
    secretMessage = ""
    for i in range(len(messageArray)):
        messageArray[i] = messageArray[i][::-1]
        secretMessage += messageArray[i] + " "
    secretMessage = secretMessage.strip()
    return secretMessage
            

#########################################

"""
Function Name: countTickets()
Parameters: aList (list)
Returns: total (int) or error message (str)
"""
def countTickets(aList):
    isCorrect = True
    tickets = 0
    maxList = []
    index = 0
    while index < len(aList):
        tickets = tickets + int(aList[index + 1])
        if int(aList[index + 1]) > 3:
            isCorrect = False
            maxList.append(aList[index])
        index = index + 2
    if isCorrect:
        output = tickets
    else:
        output = ("Sorry {}, but you can only get a maximum of three tickets per person."
                  .format(maxList[0]))
    return output


#########################################

"""
Function Name: fieldTripRoster()
Parameters: friendList (list)
Returns: nameList (list)
"""
def fieldTripRoster(friendList):
    nameList = []
    for i in range(len(friendList)):
        for j in range(3):
            if type(friendList[i][j]) == str and isUnique(friendList[i][j], nameList):
                nameList.append(friendList[i][j])
    nameList.sort()
    return nameList

def isUnique(name, nameList):
    isUnique = True
    for i in range(len(nameList)):
        if name == nameList[i]:
            isUnique = False
            break
    return isUnique

#########################################

"""
Function Name: isSublist()
Parameters: myList (list), otherList (list)
Returns: True or False (bool)
"""
def isSublist(myList, otherList):
    isSublist = False
    if len(otherList)<= 0: 
        output = True
    elif len(otherList) > len(myList):
        output = False
    else:
        for i in range(len(myList)):
            if myList[i] == otherList[0]:
                if len(myList) < len(otherList) + i:
                    break
                else:
                    for j in range(len(otherList)):
                        if myList[i + j] != otherList[j]:
                            break
                        if j == len(otherList) - 1:
                            isSublist = True
        output = isSublist
    return output
                        
            
                



