from core.player import Player 
from core.goblin import Goblin
from core.orc import Orc
from random import choice ,randint

class Game:
    def show_menu(self)-> bool:
        print("chose battel or exit\n1:battel\n0:exit")
        user_choise = input()
        while user_choise not in ["1","0"]:
            print("invalid")
            print("chose battel or exit\n1:battel\n0:exit")
            user_choise = input()
        return int(user_choise)

    def roll_dice(self,sides):
        return randint(1,sides)

    def creat_player(self):
        player = Player("dani")
        return player

    def choose_random_monster(self)->Orc | Goblin:
        monster_class = choice([Orc,Goblin])
        monster = monster_class("blublu")
        return monster
    
    def battle(self,player,monster)-> int:
        players = [player,monster]
        def chose_first():
            p_roll = self.roll_dice(6)
            m_roll = self.roll_dice(6)
            if p_roll >= m_roll:
                return 0
            return 1
        
        turn = chose_first()


        while player.hp > 0 and monster.hp > 0:
           
            attacker = players[turn % 2]
            attacked = players[(turn+1) % 2]
            
            print(f"attacker = {attacker.name} , attacked = {attacked.name}")

            dameg  = attacker.attack(attacked)
 
            print(f"{attacked.name}:hp = {attacked.hp} - damage = {dameg} = total = {attacked.hp - dameg}")

            attacked.hp -= dameg

            turn += 1

        print("player won!!") if player.hp else print("monster won!!")
        

    def start(self):
        if self.show_menu():
            player = self.creat_player()
            monster = self.choose_random_monster()
            print(player)
            print(monster)
            self.battle(player,monster)



  

