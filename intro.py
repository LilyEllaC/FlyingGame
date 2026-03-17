import constants as const
import utilities as util

def play():
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("Welcome to the flying game!", const.FONT60, const.BLACK, const.WIDTH/2, 60)
    util.toScreen("Click to start", const.FONT30, const.BLACK, const.WIDTH/2, 400)