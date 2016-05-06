import os
import sys

from Soldier import Soldier

"""docstring for Army class. The armies contents are held here.
Fields:
name - name of army
max - the amount of soldiers an army can contain
soldiers - list which contains soldier objects"""
class Army(object):
    def __init__(self, arg):
        self.__name = arg
        self.__max = 10
        self.soldiers = []
        self.defeated = False

    def getName(self):
        return self.__name

    """ countMembers - The current amount of members activated in the army """
    def countMembers(self):
        return len(self.soldiers)

    """ ableToFight - Can the army carry on? Returns True if army is able """
    def ableToFight(self):
        if self.defeated == False:
            return True
        else:
            return False

    """ admitDefeat - When last soldier has died defeat is inevitable """
    def admitDefeat(self):
        self.defeated = True
        return self.defeated

    """ currentActivateRecruit - The active soldier is 'soldiers[] -1 ' """
    def currentActiveRecruit(self):
        position = len(self.soldiers) - 1
        return (self.soldiers[position], position)

    """ maxSoldiersAllowed - Returns how many members can join an army"""
    def maxSoldiersAllowed(self):
        return self.__max
