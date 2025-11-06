from core.creature import Creature
from random import randint , choice

class Goblin(Creature):
    weapons = [('Knife',0.5), ('Sword',1) , ('Axe',1.5)]
    def __init__(self, name,roll_dice):
        super().__init__(name,roll_dice)
        self.hp = 20
        self.type = "goblin"
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = 1
        self.weapon = choice(Goblin.weapons)

    def __str__(self):
        return f"""name: {self.name}
type: {self.type}
hp :{self.hp}\nspeed: {self.speed}
power: {self.power}
armor: {self.armor_rating}
wepon: {self.weapon[0]}
        """    

    def speak(self):
        print(f"the {self.type} {self.name} is angry")

    def run_away(self)-> bool:
        if self.hp < 10:
            print(f"the {self.type} is trying to run away..")
            if randint(1,3) ==  3:
                print(f"the {self.type} run away")
                return True
            else:
                print(f"the {self.type} faild\n")   
                return False


    def attack(self, attacked, is_munster=True):
        return super().attack(attacked, is_munster)
    
  