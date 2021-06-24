#!/usr/bin/python
from weapon import Weapon

class Knight:
    def __init__(self, nm, stam, ty, hp, sc):
        self.name=nm
        self.stamina=stam
        self.saddle=True
        self.weapon=Weapon(ty, hp, sc)

    def wield(self):
        self.stamina-=self.weapon.stamina_cost
        return self.weapon.did_it_hit()

    def knight_display(self):
        if self.stamina > 0 and self.saddle==True:
            print("\"{}\" is NOT exhausted and still on the horse. Stamina left= \'{}\'".format(self.name, self.stamina))
            print("\"{}s\" weapon of choice is: {}".format(self.name, self.weapon.display()))
        elif self.stamina > 0 and self.saddle==False:
            print("\"{}\" is NOT exhausted and has been knocked off the horse. Stamina left= \'{}\'".format(self.name, self.stamina))
            print("\"{}s\" weapon of choice is: {}".format(self.name, self.weapon.display()))
        elif self.stamina <= 0 and self.saddle==True:
            print("\"{}\" IS exhausted and still on the horse. Stamina left= \'{}\'".format(self.name, self.stamina))
            print("\"{}s\" weapon of choice is: {}".format(self.name, self.weapon.display()))
        elif self.stamina <= 0 and self.saddle==False:
            print("\"{}\" IS exhausted and had been knocked off the horse. Stamina left= \'{}\'".format(self.name, self.stamina))
            print("\"{}s\" weapon of choice is: {}".format(self.name, self.weapon.display()))