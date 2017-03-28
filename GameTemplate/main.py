'''EXAMPLE MAIN'''
from testgame import TestGame
from agent import Agent
from vector import Vector2
import random

def main():
    '''main execution func'''
    game = TestGame("Test Game")
    bob = Agent("Bob")
    bob.transform.globalposition = Vector2(10, 10)
    bob.target = Vector2(300, 200)
    game.addnewobject(bob)
    # make gameobjects to participate in game
    game.run()

if __name__ == "__main__":
    main()