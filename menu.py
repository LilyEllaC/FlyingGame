import constants as const
import utilities as util
from sprites import Button


#creating the buttons
buttons=[]
gap=25
width, height=100, 100
startX=(const.WIDTH-width*3-gap*2)/2
startY=100
buttons.append(Button(width, height, startX, startY, False, "1"))
buttons.append(Button(width, height, startX+(width+gap), startY, True, "2"))
buttons.append(Button(width, height, startX+(width+gap)*2, startY, True, "3"))
buttons.append(Button(width, height, startX, startY+(height+gap), True, "4"))
buttons.append(Button(width, height, startX+(width+gap), startY+(height+gap), True, "5"))
buttons.append(Button(width, height, startX+(width+gap)*2, startY+(height+gap), True, "6"))
buttons.append(Button(width, height, startX, startY+(height+gap)*2, True, "7"))
buttons.append(Button(width, height, startX+(width+gap), startY+(height+gap)*2, True, "8"))
buttons.append(Button(width, height, startX+(width+gap)*2, startY+(height+gap)*2, True, "9"))
buttons.append(Button(width, height, startX+(width+gap), startY+(height+gap)*3, True, "10"))




def run():
    const.SCREEN.fill(const.YELLOW)

    util.toScreen("Choose your level", const.FONT30, const.RED, const.WIDTH/2, 30)
    for button in buttons:
        button.display()
        button.checkIfHovered()

