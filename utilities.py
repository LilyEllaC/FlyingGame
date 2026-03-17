import constants as const
import pygame

#code to put text to the screen
def toScreen(words, font, colour, x, y):
    text = font.render(words, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    const.SCREEN.blit(text, textRect)

# versions to push more than 1 line
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height() // 2)
    toScreen(words2, font, colour, x, y + font.get_height() // 2)

def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y + font.get_height())

def toScreenSize(words, size, colour, x, y):
    text = pygame.font.Font("freesansbold.ttf", size).render(words, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    const.SCREEN.blit(text, textRect)

#text to put an image to the screen
def imageToScreen(imageName, x, y, width, height):
    image = pygame.image.load(imageName)
    image = pygame.transform.scale(image, (width, height))
    const.SCREEN.blit(image, (x, y))
