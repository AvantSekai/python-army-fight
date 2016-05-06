import random

""" Class to contain an individual soldiers contents """
class Soldier(object):
    def __init__(self):
        self.alive = True
        self.__weapon = ""
        self.__weapon_pwr = 1
        self.__luck = 1
        self.__attack_pwr = 1

    """ chooseWeapon - Weapon is chosen at random with a
    range of weapon_pwr associated with the weapon"""
    def chooseWeapon(self):
        # Choice of weapon is random
        weapon_list = ['knife', 'gun', 'grenade']
        self.__weapon = random.choice(weapon_list)
        # Assign weapon_pwr dependent on weapon type within the weapons range
        if self.__weapon == 'knife':
            self.__weapon_pwr = random.choice(range(1,3))
        elif self.__weapon == 'gun':
            self.__weapon_pwr = random.choice(range(4,6))
        else: # Grenade is the only choice left
            self.__weapon_pwr = random.choice(range(7,9))

    """ getWeapon - Returns the weapon currently possed by the soldier"""
    def getWeapon(self):
        return self.__weapon

    """ gainLuck - Luck is a factor that can aid little or greatly in determining
    the outcome of a battle """
    def gainLuck(self):
        # Range of luck is determined by the weapon range of damage
        # The more damage a weapon has the less luck is needed
        lknife_range = range(1,9)
        lgun_range = range(1,6)
        lgrenade_range = range(1,3)

        if self.__weapon == 'knife':
            self.__luck = random.choice(lknife_range)
        elif self.__weapon == 'gun':
            self.__luck = random.choice(lgun_range)
        else: # Grenade is the only choice left
            self.__luck = random.choice(lgrenade_range)

    """ deadOrAlive - Check Soldier status to see if DOA (dead or alive) """
    def isAlive(self):
        if self.alive == True:
            return True
        else:
            return False

    """ calculateAtkPwr - weapon_pwr combined with luck gathers attackPwr """
    def calculateAtkPwr(self):
        atkAttributes = self.__weapon_pwr + self.__luck
        self.__attack_pwr = atkAttributes
        return self.__attack_pwr

    """ die - Soldier has been defeated and is no longer alive """
    def die(self):
        self.alive = False
        return self.alive
