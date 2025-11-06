from abc import abstractmethod
from time import sleep
from random import randint

class Creature:
    def __init__(self,name:str,roll_dice):
        self.name = name
        self.roll_dice = roll_dice

    @abstractmethod
    def speak(self):
        pass

    def Attack_speed(self)->int:
        print("checking attack speed...")
        sleep(2)
        roll = self.roll_dice(20)
        Attack_speed = roll + self.speed
        return Attack_speed 
    
    def attack(self,attacked,is_munster=False) -> int:
        def damage(self,is_munster=False)-> int:
            print("hit!!\n")
            print("checkin attack damage\n")
            roll = self.roll_dice(6)
            Attack_strength = roll + self.power
            if is_munster:
                weapon_damage = self.weapon[1]
                Attack_strength *= weapon_damage
            print(f"Attack damage = {Attack_strength}\n")
            sleep(2)
            return Attack_strength  
        
        print("checking if hit....\n")
        sleep(2)
        Attack_speed = self.Attack_speed()
        print(f"attacker speeed = {Attack_speed}")
        print(f"attacked armor = {attacked.armor_rating}\n")
        sleep(2)
        if Attack_speed > attacked.armor_rating:  
            return damage(self,is_munster)
        print("miss!")
        return 0


        
    
