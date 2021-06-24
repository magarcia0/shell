#!/usr/bin/python
from knight import Knight
def main():
    name = input("What is the first knight's name? ")
    stamina = int(input("what is \"{}'s\" stamina? ".format(name)))
    weapon_type = input("what type of weapon will \"{}\" use? ".format(name))
    stamina_cost = int(input("How much stamina does the \"{}\" drain? ".format(weapon_type)))
    hit_chance = int(input("What is the probability that the \"{}\" will hit its opponent? ".format(weapon_type)))
    k1=Knight(name, stamina, weapon_type, hit_chance, stamina_cost)

    name = input("\nWhat is the second knight's name? ")
    stamina= int(input("what is \"{}'s\" stamina? ".format(name)))
    weapon_type = input("what type of weapon will \"{}\" use? ".format(name))
    stamina_cost = int(input("How much stamina does the \"{}\" drain? ".format(weapon_type)))
    hit_chance = int(input("What is the probability that the \"{}\" will hit its opponent? ".format(weapon_type)))
    k2=Knight(name, stamina, weapon_type, hit_chance, stamina_cost)

    round=1
    while (k1.saddle==True and k2.saddle==True) and (k1.stamina > 0 and k2.stamina > 0):
        print("---------------------------------")
        print("            [ Round ]")
        print("[:::]======>    {}   <======[:::]".format(round))
        print("---------------------------------")
        if k1.wield()==True:
            k2.saddle=False
        if k2.wield()==True:
            k1.saddle=False
        k1.knight_display()
        k2.knight_display()
        print("---------------------------------")
        round+=1
if __name__=="__main__":
    main()