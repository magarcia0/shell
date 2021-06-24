#!/user/bin/env python3
from random import randint

class Weapon:
    def __init__(self, ty, hp, sc):
        self.weapon_type=ty
        self.hit_probability=hp
        self.stamina_cost=sc

    def display(self):
        return "\"{}\" that requires \'{}\' stamina and has a \'{}%\' chance to hit".format(self.weapon_type, self.stamina_cost, self.hit_probability)

    def did_it_hit(self):
        randy = randint(1,100)
        if randy <= self.hit_probability:
            return True
        return False