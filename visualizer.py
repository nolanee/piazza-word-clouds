import pygame, sys


def initializeScreen(caption, screenWidth, screenHeight, backgroundColor):
    '''
    * Requires: caption is a string.
    *           screenWidth and screenHeight are integers.
    *           screenWidth > 0, screenHeight > 0.
    *           backgroundColor is a tuple of integers (r,g,b).
    *           r >= 0, g >= 0, b >= 0.
    * Modifies: Nothing.
    * Effects:  Returns an initialized and titled screen.
    '''
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    screen.fill(backgroundColor)
    pygame.display.update()
    pygame.display.set_caption(caption)
    return screen


if __name__=='__main__':
    white = (255, 255, 255)
    screen = initializeScreen("Snow White", 640, 480, white)
    # This is test code that should run the first time you run "python visualizer.py"
    # Expected output is a window of size 640 by 480 pixels, with white background, and title "Snow White".



