"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: intramuralGames()
Parameters: gameName (str), numFriends (int)
Returns: None (NoneType)
"""
def intramuralGames(gameName, numFriends):
    if numFriends < 0 or numFriends > 7:
        return
    elif numFriends < 2:
        output = "Let's choose something else."
    elif numFriends < 6:
        output = ("We will try out {} for a little bit!".format(gameName))
    else:
        output = ("Let's register for {}!!!".format(gameName))

    print(output)

#########################################

"""
Function Name: goShopping()
Parameters: item (str), quantity (int), budget (float)
Returns: moneyLeft (float) or error message (str)
"""
def goShopping(item, quantity, budget):
    if item == "Shorts":
        price = 13
    elif item == "T-Shirts and Tanks":
        price = 9.75
    elif item == "Swimwear":
        price = 20.00
    elif item == "Sunglasses":
        price = 7.50
    elif item == "Slides":
        price = 15.50
    else:
        return

    remaining = budget - price * quantity
    
    if remaining > 0:
        output = remaining
    else:
        output = "Not enough money!"

    return output

#########################################

"""
Function Name: getDinner()
Parameters: budget (float), diningOption (str)
Returns: restaurantName (str)
"""
def getDinner(budget, diningOption):
    if budget < 0 or budget > 40:
        return
    
    elif budget <= 10:
        if diningOption == "Takeout" or diningOption == "Delivery":
            restaurantName = "Chick Fil A"
        elif diningOption == "Indoor" or diningOption == "Outdoor":
            restaurantName = "Moe's"
        else:
            return

    elif budget <= 20:
        if diningOption == "Indoor" or diningOption == "Takeout":
            restaurantName = "Tin Drum"
        elif diningOption == "Outdoor" or diningOption == "Delivery":
            restaurantName = "Umma's"
        else:
            return

    elif budget <= 30:
        if diningOption == "Indoor" or diningOption == "Outdoor" or diningOption == "Takeout":
            restaurantName = "Yeah Burger"
        elif diningOption == "Delivery":
            restaurantName = "Flip Burger"
        else:
            return

    else:
        if diningOption == "Indoor":
            restaurantName = "Two Urban Licks"
        elif diningOption == "Delivery" or diningOption == "Outdoor" or diningOption == "Takeout":
            restaurantName = "Gypsy Kitchen"
        else:
            return

    return restaurantName
    
#########################################

"""
Function Name: backupRestaurant()
Parameters: budget (float), diningOption (str), backup (str)
Returns: decision (str)
"""
def backupRestaurant(budget, diningOption, backup):
    prefRestaurant = getDinner(budget, diningOption)

    if findTime(prefRestaurant) > findTime(backup):
        output = ("You'll have to get dinner at {} instead.".format(backup))
    else:
        output = ("Yay, you can get dinner at your first choice, {}.".format(prefRestaurant))

    return output

def findTime(restaurant):
    if restaurant == "None":
        return
    elif restaurant == "Chick Fil A" or restaurant == "Umma's" or restaurant == "Gypsy Kitchen" or restaurant == "Flip Burger":
        time = 15
    else:
        time = 45

    return time
    
#########################################

"""
Function Name: rideShare()
Parameters: number of riders (int), miles(int), rideShareOptionaA (str), rideShareOptionaB (str)
Returns: rideShareOption (str)
"""
def rideShare(numRiders, miles, rideShareA, rideShareB):
    if determineCost(rideShareA, numRiders, miles) <= determineCost(rideShareB, numRiders, miles):
        output = rideShareA
    else:
        output = rideShareB

    return output

def determineCost(rideShare, numRiders, miles):
    if rideShare == "Uber":
        cost = 5 + 5.5 * miles
        if numRiders > 3:
            cost = cost - 5
    elif rideShare == "Lyft":
        cost = 10 + 1.5 * miles
    elif rideShare == "Hitch":
        cost = 7.5 * miles
        if numRiders > 2:
            cost = cost - 10 * numRiders
    elif rideShare == "Taxi":
        cost = 18 * miles

    return cost


