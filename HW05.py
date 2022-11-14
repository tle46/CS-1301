"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""

#########################################

"""
Function Name: dinnerParty()
Parameters: list of names and availabilities (list), day (str)
Returns: list of friends (list)
"""
def dinnerParty(avail, day):
    i = 1
    availibleName = []
    for i in range(len(avail)):
        if day in avail[i][1]:
            availibleName.append(avail[i][0])
    return availibleName

#########################################

"""
Function Name: whatShouldIWear()
Parameters: list of temperatures (list), list of recommendations (list)
Returns: list of tuples (list)
"""
def whatShouldIWear(temp, rec):
    outputList = []
    for i in range(len(temp)):
        outputList.append((temp[i],rec[i]))
    return outputList

#########################################

"""
Function Name: cheapMeals()
Parameters: list of strings (list) and budget (float)
Returns: tuple containing menu items (tuple)
"""
def cheapMeals(menuList, budget):
    nameList = []
    priceList = []
    for i in range(len(menuList)):
        menuList[i] = menuList[i].split(" - $")
        priceList.append(float(menuList[i][1]))

    priceList.sort()

    for i in range(len(priceList)):
        if priceList[i] > budget:
            break
        else:
            for j in range(len(menuList)):
                if float(menuList[j][1]) == priceList[i]:
                    nameList.append(menuList[j][0])
                    break

    return tuple(nameList)
    
#########################################

"""
Function Name: wednesdays()
Parameters: list of tuples with dates and holidays (list)
Returns: list of holidays (list)
"""
import calendar

def wednesdays(holidayList):
    wedHolidayList = []
    for holiday in holidayList:
        if calendar.weekday(holiday[3], holiday[2], holiday[1]) == 2:
            wedHolidayList.append(holiday[0])
    return wedHolidayList

#########################################

"""
Function Name: starbucksFanatic()
Parameters: list of starbucks menu items (list)
Returns: list of tuples containing menu item name and price (list)
Returns: True or False (bool)
"""
import starbucks

def starbucksFanatic(nameList):
    menuList = []
    totSum = 0

    for name in nameList:
        if starbucks.menu(name) > 0:
            menuList.append((name, starbucks.menu(name)))
            totSum += starbucks.menu(name)

    menuList.append(round(totSum, 2))
    return menuList
