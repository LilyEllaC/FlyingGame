import constants as const
import utilities as util
from sprites import Player

#creating the player
player=Player(50,50,400,400, 100/const.FPS+1, 5/const.FPS+1, 2/const.FPS)



def play():
    player.move()
    player.display()

