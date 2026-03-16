import constants as const
import sprites
import utilities as util
import gameplay 
import intro

#actual important stuff
import pygame
import asyncio
# pylint: disable=no-member
pygame.init()
running=True
clock= pygame.time.Clock()


#actual main function
async def main():
    global running
    gameState="playing"

    while running:
        for event in pygame.event.get():
            #getting the x to close tha game
            if event.type == pygame.QUIT:
                running = False

            #if the game is playing
            if gameState=="playing":
                if event.type==pygame.KEYDOWN:
                    gameplay.player.startMove(event.key)
                if event.type==pygame.KEYUP:
                    gameplay.player.stopMove(event.key)
        

        #stuff
        const.SCREEN.fill(const.TEAL)
        if gameState=="intro":
            intro.play()
        elif gameState=="playing":
            gameplay.play()

        #showing the FPS
        util.toScreen("FPS:"+str(clock.get_fps()), const.FONT40, const.RED, const.WIDTH/2, 50)

        #important ending stuff
        pygame.display.flip()
        clock.tick(const.FPS)
        await asyncio.sleep(0)



if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
