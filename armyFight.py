import os
import sys
import string

from Army import Army
from Soldier import Soldier

""" initiateRecruit - Creates a new Soldier for the army to go into battle"""
def initiateRecruit():
    new_recruit = Soldier()
    weapon = new_recruit.chooseWeapon()
    luck = new_recruit.gainLuck()
    return new_recruit

""" Check soldier in battle condition"""
def checkSoldierStatus(recruit, army):
    if recruit.isAlive == False:
        army.soldiers.append(initiateRecruit())
    return recruit, army

""" Check armies condition to continue battle"""
def checkArmyStatus(army):
    if army.countMembers() == 0:
        # Prep first soldier to fight
        army.soldiers.append(initiateRecruit())
        print "# of recruits who joined the fight is %d for %s army " % (army.countMembers() ,army.getName())
    elif army.countMembers() <= army.maxSoldiersAllowed():
        # Army is still in the fight Carry Onward!
        print "The fight continues on.... for %s army" % army.getName()
    else: # Means max number of soldiers have been reached
        recruit_soldier, num_soldier = army.currentActiveRecruit()
        if recruit_soldier.isAlive == True:
            #keep fighting
            print "Fight on %s soldier %d!" %(recruit_soldier.getName(), num_soldier)
        else:
            #Army has been defeated
            print "%s army has been defeated" % army.getName()
            army.admitDefeat()
            #endbattle
    return army

""" fight - Determines between the soldiers who wins a battle """
def fight(red_soldier, red_num, blue_soldier, blue_num):
    reds_power = red_soldier.calculateAtkPwr()
    blues_power = blue_soldier.calculateAtkPwr()
    # If Red is stronger it kills blue soldier
    if reds_power > blues_power:
        print "Red Soldier %d kills Blue Soldier %d with a %s an attack power of %d" \
            % (red_num, blue_num, red_soldier.getWeapon(), reds_power)
        blue_soldier.die()
        print "Blue soldier %s" % blue_soldier.isAlive()
    # blue is stronger it kills red soldier
    elif blues_power > reds_power:
        print "Blue Soldier %d gets the upper hand on Red Soldier %d using a %s and attack power of %d" \
        % (blue_num, red_num, blue_soldier.getWeapon(), blues_power)
        red_soldier.die()
        print "Red soldier %s" % red_soldier.isAlive()
    else: # They have eliminated each other
        print "It's a draw to the death!"
        red_soldier.die()
        blue_soldier.die()
    return red_soldier, blue_soldier


"""Run - Game Engine for Handeling Game Events """
def run(red, blue):
    # While armies are still able and willing...  Fight ON!
    red = checkArmyStatus(red)
    blue = checkArmyStatus(blue)
    if (red.ableToFight() and blue.ableToFight()):
        print "red members %d blue members %d" %(red.countMembers(), blue.countMembers())
        red_soldier, red_num = red.currentActiveRecruit()
        blue_soldier, blue_num = blue.currentActiveRecruit()
        red_soldier, blue_soldier = fight(red_soldier, red_num, blue_soldier, blue_num)

        if red_soldier.isAlive():
            # continue - nothing has changed
            print "Red soldier %d lives to fight another day!" % (red_num)
        # Is red still able to fight?
        else:
            red_soldier, red = checkSoldierStatus(red_soldier, red)
            red = checkArmyStatus(red)
            print "What do we do now red?"
            red.soldiers.append(initiateRecruit())
        if blue_soldier.isAlive():
            # continue
            print "Blue soldier %d lives to fight another day!" % (blue_num)
        # Is blue still able to fight?
        else:
            blue_soldier, blue = checkSoldierStatus(blue_soldier, blue)
            blue = checkArmyStatus(blue)
            print "What do we do now blue?"
            blue.soldiers.append(initiateRecruit())
        # Run the next battle sequence
        run(red, blue)
    else:
        # Declare a winner
        if red.ableToFight():
            print "Red Army wins the battle"
        else:
            print "Blue Army wins the battle"

if __name__ == "__main__":
    # Create two oppossing armies to fight
    red = Army("red")
    #print "%s army has %d soldiers who fought" % (red.getName(), red.countMembers())
    blue = Army("blue")
    #print "%s army has %d soldiers who fought" % (blue.getName(), blue.countMembers())
    run(red, blue)
