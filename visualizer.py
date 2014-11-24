import pygame, sys


def getTfidfDictionary(singlePiazzaPost):
    '''
    * Requires: singlePiazzaPost is a piazzaPost object.
    * Modifies: Nothing.
    * Effects:  Returns a dictionary of words/phrases as keys,
    *           and their tfidf as values.
    '''


def binPiazzaPosts(piazzaPostDict, phrases):
    '''
    * Requires: piazzaPostDict is a dictionary of piazzaPost objects.
    *           It has string keys, and piazzaPost objects as values.
    *           Keys are IDs of piazzaPost objects.
    *
    *           phrases is a boolean.
    *           When True, return phrases (collocations).
    *           When False, return words.
    *
    * Modifies: Nothing.
    *
    * Effects:  Bins the posts according to days/weeks.
    *           Returns a dictionary of dictionaries.
    *           Keys are dates/weeks.
    *           Values are dictionaries of words/phrases, with their tfidfs.
    *           If phrases = True, returns phrases. Else returns words.
    *
    * Calls:    getTfidfDictionary
    '''


def drawWordCloud(binnedDict, baseFontSize):
    '''
    * Requires: binnedDict is a dictionary with string keys and float values.
    *           baseFontSize is an integer > 0.
    *           binnedDict has words/phrases as keys, and their tfidf as values.
    *           baseFontSize is the size of the smallest allowable font.
    * Modifies: Nothing.
    * Effects:  Returns a word cloud surface.
    '''


def drawTimeLine(piazzaPostDict, baseFontSize, phrases = False):
    '''
    * Requires: piazzaPostDict is a dictionary of piazzaPost objects.
    *           It has string keys, and piazzaPost objects as values.
    *           Keys are IDs of piazzaPost objects.
    *
    *           phrases is a boolean.
    *           When True, return phrases (collocations).
    *           When False, return words.
    *
    *           baseFontSize is an integer > 0.
    *           It is the size of the smallest allowable font.
    *
    * Modifies: Nothing.
    * Effects:  Returns a timeline surface (to be blitted onto screen).
    *           The timeline surface consists of multiple word clouds,
    *           each one for a separate bin.
    *
    * Calls:    binPiazzaPosts
    *           drawWordCloud
    '''


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
    '''
    * Requires: Nothing.
    * Modifies: Nothing.
    * Effects:  Draws an animated timeline on a screen.
    *
    *           The function MUST implement a loop that
    *           goes through and highlights each word
    *           cloud in turn.
    *
    * Calls:    initializeScreen
    *           drawTimeLine
    '''
    white = (255, 255, 255)
    screen = initializeScreen("Snow White", 640, 480, white)
    # This is test code that should run the first time you run "python visualizer.py"
    # Expected output is a window of size 640 by 480 pixels, with white background, and title "Snow White".



