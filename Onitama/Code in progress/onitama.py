#!/usr/bin/env python
#cd
#
#
#
#

# documentation string of this module
"""
Minimal pygame program.
"""
# some informational variables
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 109 $"
__date__      = "$Date: 2007-04-03 18:00:40 +0200 (Di, 03 Apr 2007) $"
__license__   = ''
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"

#----------------------------- actual code --------------------------------


import pygame


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Onitama")

    # create a surface on screen that has the size of 1000 x 1000
    screen = pygame.display.set_mode((1000,1000))

    # define a variable to control the main loop
    running = True

    # define background checkerboard
    image = pygame.image.load("Checkerboard.png")
    card1 = pygame.image.load("frog.jpg")

    screen.fill((255,255,204))
    screen.blit(image, (250,250))
    screen.blit(card1,(300,800))
    screen.blit(card1,(550,800))

    pygame.display.update()


    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False # user pressed ESC
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print (pygame.mouse.get_pos())

if __name__=="__main__":
    # call the main function
    main()
