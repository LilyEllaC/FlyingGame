import constants as const
import utilities as util
from sprites import Player
#levels
from levels import level1
from levels import level2
from levels import level3
from levels import level4
from levels import level5
from levels import level6
from levels import level7
from levels import level8
from levels import level9
from levels import level10

#creating the player
player=Player(50,50,400,400, 100/const.FPS+1, 3/const.FPS+1, 2/const.FPS)
level="0"

levels=[level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]

def play():
    levels[int(level)-1].play()


    player.move()
    player.display()

