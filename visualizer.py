import pygame, sys
from indexer import *


def binPiazzaPosts(index, phrases):
    '''
    * Requires: index is an Indexer() object.
    *
    *           phrases is an integer (1 to 4).
    *           When phrases = 1, return words (unigrams).
    *           When phrases = 2, return bigrams
    *           When phrases = 3, return trigrams.
    *           When phrases = 4, return fourgrams.
    *
    * Modifies: Nothing.
    *
    * Effects:  Bins the posts according to weeks.
    *           Returns a dictionary of dictionaries.
    *           Keys are dates/weeks.
    *           Values are dictionaries of words/phrases, with their tfidfs.
    *           idf has already been computed by the indexer, but you
    *           will need to compute the tf's in each bin for each word.
    *           If phrases = True, returns phrases. Else returns words.
    '''


def drawWordCloud(singleBinDict, baseFontSize):
    '''
    * Requires: singleBinDict is a dictionary with string keys and float values.
    *           baseFontSize is an integer > 0.
    *           singleBinDict has words/phrases as keys,
    *                         and their tfidf as values.
    *           baseFontSize is the size of the smallest allowable font.
    * Modifies: Nothing.
    * Effects:  Returns a word cloud surface (to be blitted onto the
                                              timeline surface below)
    *           SEE README FOR DETAILS
    '''


def drawTimeLine(index, baseFontSize, phrases = 1):
    '''
    * Requires: index is an Indexer() object.
    *
    *           phrases is an integer (1 to 4).
    *           When phrases = 1, return words (unigrams).
    *           When phrases = 2, return bigrams
    *           When phrases = 3, return trigrams.
    *           When phrases = 4, return fourgrams.
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
    *           SEE README FOR DETAILS
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


def dummyIndex(index):
    '''
    * Requires: index is an Indexer() object
    * Modifies: Sets the tfidfDict member variable of index
    * Effects: Nothing. This is just here for testing BEFORE indexer is finished
    *          Forgive the wretched style
    '''
    index.posts = {1 : "love java black", 2 : "need drink java", 3 : "love drink java", 4 : "travel java islands",5 : "travel agent java islands", 6 : "see travel java"}
    index.idfDict = {'love drink': 0.7781512503836436, 'travel agent': 0.7781512503836436, 'java': 0.0, 'see travel': 0.7781512503836436, 'travel java': 0.47712125471966244, 'drink java': 0.47712125471966244, 'love java': 0.7781512503836436, 'travel': 0.3010299956639812, 'drink': 0.47712125471966244, 'see': 0.7781512503836436, 'agent': 0.7781512503836436, 'need drink': 0.7781512503836436, 'java islands': 0.47712125471966244, 'agent java': 0.7781512503836436, 'black': 0.7781512503836436, 'islands': 0.47712125471966244, 'need': 0.7781512503836436, 'love': 0.47712125471966244, 'java black': 0.7781512503836436}



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
    index = Indexer()
    #TODO: Make idf calculations in indexer.py
    dummyIndex(index) #replace this once indexer is finished
    white = (255, 255, 255)
    screen = initializeScreen("Snow White", 640, 480, white)
    # This is test code that should run the first time you run "python visualizer.py"
    # Expected output is a window of size 640 by 480 pixels, with white background, and title "Snow White".



