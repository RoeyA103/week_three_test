from abc import abstractmethod
from time import sleep
from random import randint

class Creature:
    def __init__(self,name:str):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def roll_dice(self,sides):
        return randint(1,sides)

    def Attack_speed(self)->int:
        print("checking attack speed...")
        sleep(2)
        roll = self.roll_dice(20)
        Attack_speed = roll + self.speed
        return Attack_speed 
    
    def attack(self,attacked,is_munster=False) -> int:
        def damage(self,is_munster=False)-> int:
            print("hit!!")
            print("checkin attack strength")
            roll = self.roll_dice(6)
            Attack_strength = roll + self.power
            if is_munster:
                weapon_damage = self.weapon[1]
                Attack_strength *= weapon_damage
            print(f"Attack strength = {Attack_strength}")
            sleep(2)
            return Attack_strength  
        
        print("checking if hit....")
        sleep(2)
        Attack_speed = self.Attack_speed()
        print(f"attacker speeed = {Attack_speed}")
        print(f"attacked armor = {attacked.armor_rating}")
        sleep(2)
        if Attack_speed > attacked.armor_rating:  
            return damage(self,is_munster)
        print("miss!")
        return 0


        
    
