import constants as const
import sprites
import utilities

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

    while running:
        for event in pygame.event.get():
            #getting the x to close tha game
            if event.type == pygame.QUIT:
                running = False
        
        const.SCREEN.fill(const.TEAL)

        #important ending stuff
        pygame.display.flip()
        clock.tick(const.FPS)
        await asyncio.sleep(0)



if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
