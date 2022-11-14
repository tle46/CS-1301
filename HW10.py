"""
Georgia Institute of Technology - CS1301
Homework 10 - Object Oriented Programming
"""

class Pokemon:
    def __init__(self, name, level, pokeType, bag, health = 50, isAlive = True):
        self.name = name
        self.level = level
        self.type = pokeType
        self.bag = bag
        self.health = health
        self.isAlive = isAlive
        
    def loseHealth(self, healthLost):
        if self.isAlive:
            self.health -= 5 * healthLost
        if self.health <= 0:
            self.isAlive = False
            
    def gainHealth(self):
        if self.isAlive:
            if self.bag.healthPotion > 0:
                if self.health <= 30:
                    self.health += 20
                else:
                    self.health = 50
                self.bag.healthPotion -= 1
            else:
                print("Sorry, {} has no health potions!".format(self.name))
        else:
            print("{} has fainted! Cannot gain health!".format(self.name))

    def surrender(self):
        self.bag.whiteFlag = True

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __str__(self):
        return ("This is {} type Pokemon {} with level {}, current health is {}."
              .format(self.type, self.name, self.level, float(self.health)))
        
#########################################################


class Bag:
    def __init__(self, healthPotion, whiteFlag):
        self.healthPotion = healthPotion
        self.whiteFlag = whiteFlag
    
    def __eq__(self, other):
        return self.healthPotion == other.healthPotion and self.whiteFlag == other.whiteFlag


#########################################################


class Lobby:
    def __init__(self, roomName, pokeA, pokeB):
        self.roomName = roomName
        self.pokeA = pokeA
        self.pokeB = pokeB

    def battle(self):
        if self.pokeA.type == self.pokeB.type:
            self.pokeA.loseHealth(1)
            self.pokeB.loseHealth(1)
        elif (self.pokeA.type == "Fire" and self.pokeB.type == "Water") or (self.pokeA.type == "Water" and self.pokeB.type == "Grass") or(self.pokeA.type == "Grass" and self.pokeB.type == "Fire"):
            self.pokeA.loseHealth(2)
            self.pokeB.loseHealth(0.5)
        else:
            self.pokeA.loseHealth(0.5)
            self.pokeB.loseHealth(2)
        self.gameOver()

    def gameOver(self):
        if (self.pokeA.isAlive == False and self.pokeB.isAlive == False) or self.pokeA.bag.whiteFlag == True and self.pokeB.bag.WhiteFlag == True:
            print("It's a tie!")
        elif (self.pokeA.isAlive == False or self.pokeA.bag.whiteFlag == True) and self.pokeB.isAlive:
            print("{} won the battle".format(self.pokeB.name))
            self.pokeA.bag.whiteFlag == False
        elif (self.pokeB.isAlive == False or self.pokeB.bag.whiteFlag == True) and self.pokeA.isAlive:
            print("{} won the battle".format(self.pokeA.name))
            self.pokeB.bag.whiteFlag == False
        
    def __eq__(self, other):
        return self.roomName == other.roomName

    
        
