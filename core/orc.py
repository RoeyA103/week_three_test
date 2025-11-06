from core.creature import Creature
from random import randint , choice

class Orc(Creature):
    weapons = [('Knife',0.5), ('Sword',1) , ('Axe',1.5)]
    def __init__(self, name,roll_dice):
        super().__init__(name,roll_dice)
        self.hp = 20
        self.type = "orc"
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = 1
        self.weapon = choice(Orc.weapons)

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

    def attack(self, attacked, is_munster=True):
        return super().attack(attacked, is_munster)        