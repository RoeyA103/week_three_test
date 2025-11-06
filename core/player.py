from random import randint , choice
from core.creature import Creature

class Player(Creature):
    profession = ['warrior','healer']
    def __init__(self,name:str):
        super().__init__(name)
        self.profession = choice(Player.profession)
        self.hp = 50 
        self.speed = randint(5,10)
        self.power = randint(5,10) 
        self.armor_rating = randint(5,15)
        self.profession = choice(Player.profession)
        if self.profession == 'warrior':
            self.power += 2
        else:
            self.hp += 10

    def __str__(self):
        return f"""name: {self.name}
profession: {self.profession}
hp :{self.hp}\nspeed: {self.speed}
power: {self.power}
armor: {self.armor_rating}\n
        """
    
    def attack(self, attacked, is_munster=False):
        return super().attack(attacked, is_munster=False)
