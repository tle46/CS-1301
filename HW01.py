"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: clubPoints()
Parameters: N/A
Returns: None
"""
def clubPoints():
    clubs = int(input("How many clubs have you joined? "))
    friends = int(input("How many friends have you gotten to join clubs? "))
    points = 30 * clubs + 50 * friends
    print("You have won a total of {} points!!".format(points))

#########################################

"""
Function Name: moveIn()
Parameters: N/A
Returns: None
"""
def moveIn():
    freshman = int(input("How many freshmen do you plan to assist? "))
    sophomore = int(input("How many sophomores do you plan to assist? "))
    junior = int(input("How many juniors do you plan to assist? "))

    students = freshman + sophomore + junior

    minutes = freshman * 35 + sophomore * 20 + junior * 15

    hours = minutes // 60
    minutes = minutes % 60
    
    print("It will take {} hours and {} minutes to help {} students with move-in today.".format(hours, minutes, students))
    

#########################################

"""
Function Name: tireArea()
Parameters: N/A
Returns: None
"""
def tireArea():
    radius = float(input("What is the radius of the tire? "))

    area = round(3.14 * radius ** 2, 2)
    
    print("The area of the tire is {}.".format(area))

#########################################

"""
Function Name: dining()
Parameters: N/A
Returns: None
"""
def dining():
    pFood = int(input("How many meals do you want to order from Panda Express? "))
    rFood = int(input("How many meals do you want to order from Rising Roll? "))
    cFood = int(input("How many meals do you want to order from Chick-fil-A? "))
    tipPercent = int(input("What percent would you like to tip? "))

    baseCost = pFood * 6 + rFood * 8 + cFood * 9

    tip = round(baseCost * 0.01 * tipPercent, 2)

    total = baseCost + tip
    
    print("You paid ${} and tipped ${}.".format(total, tip))

#########################################

"""
Function Name: weeklyBudget()
Parameters: N/A
Returns: None
"""
def weeklyBudget():
    budget = int(input("How much is your budget this week? "))
    savePercent = int(input("What percentage do you want to save? "))
    
    budget = budget * (1 - (0.01 * savePercent))
    budget = budget - 34.9

    budget = round(budget, 2)

    print("You have ${} left after savings and fees.".format(budget))



