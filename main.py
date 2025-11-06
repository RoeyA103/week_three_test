from core.player import Player 
from core.goblin import Goblin
from core.orc import Orc
from random import choice ,randint
from game import Game

def main():
    game = Game()
    game.start()
    

if __name__ == "__main__":
    main()