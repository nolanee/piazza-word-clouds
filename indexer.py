from piazzaPost import *

def getBigrams(listOfWords):
    '''
    * Requires: listOfWords is a list of strings.
    * Modifies: Nothing.
    * Effects:  Returns a list of bigrams.
    '''



def getTrigrams(listOfWords):
    '''
    * Requires: listOfWords is a list of strings.
    * Modifies: Nothing.
    * Effects:  Returns a list of trigrams.
    '''



def getFourgrams(listOfWords):
    '''
    * Requires: listOfWords is a list of strings.
    * Modifies: Nothing.
    * Effects:  Returns a list of fourgrams.
    '''



def sortListByFrequency(listOfNGrams):
    '''
    * Requires: listOfNGrams is a list of strings.
    * Modifies: Nothing.
    * Effects:  Returns a sorted list of n-grams.
    *           Sorting is in descending order of frequency.
    '''



def removePunctuation(text):
    '''
    * Requires: text is a string.
    * Modifies: Nothing.
    * Effects:  Removes all punctuation from text and returns it.
    '''



def removeStopWords(listOfWords, dictOfStopWords):
    '''
    * Requires: listOfWords is a list of strings.
    *           dictOfStopWords is a dictionary with strings as keys.
    * Modifies: Nothing.
    * Effects:  Removes all stop words from the list of words and returns the list.
    '''



def removeStopWordsFromNGrams(listOfNGrams, dictOfStopWords):
    '''
    * Requires: listOfNGrams is a list of strings.
    *           dictOfStopWords is a dictionary with strings as keys.
    * Modifies: Nothing.
    * Effects:  Removes all n-grams (from the list of n-grams) that
    *           start or end with a stop word, and returns the list.
    '''



def lowerCase(text):
    '''
    * Requires: text is a string.
    * Modifies: Nothing.
    * Effects:  Lowercases text and returns it.
    '''



def tokenize(text):
    '''
    * Requires: text is a string.
    * Modifies: Nothing.
    * Effects:  Splits text on whitespace delimiter and returns a list of words.
    '''



def writeOut(filename, listOfNGrams, extension):
    '''
    * Requires: filename is a string (filename).
    *           listOfNGrams is a list of tuples:
    *           - tuple[1] is an n-gram (string).
    *           - tuple[0] is frequency of the n-gram (int).
    *           extension is one of ["unigrams", "bigrams", "trigrams", "fourgrams"].
    * Modifies: Nothing.
    * Effects:  Opens a file in write mode with filename and appropriate extension.
    *           Writes n-grams and frequency in following format:
    *           nGram_1_count nGram_1
    *           nGram_2_count nGram_2
    *           nGram_3_count nGram_3
    *           ...
    *           Closes the file.
    '''



def getStopWords(stopFileName):
    '''
    * Requires: stopFileName is a string (filename).
    *           The file with this name must exist in project directory.
    * Modifies: Nothing.
    * Effects:  Opens the stop words file in read mode.
    *           Reads stop words from the file.
    *           Creates a dictionary with stop words as keys.
    *           Closes the file.
    *           Returns the dictionary.
    '''


def readPiazzaData(fname):
    '''
    * Requires: fname is the name of the Piazza data to be read in.
    * Modifies: Nothing.
    * Effects:  Returns a dictionary of {ID:PiazzaPost} pairs. ID is a string.
    '''
    #Open the file and read all lines
    F = open(fname,"r")
    lines = F.readlines()
    F.close()

    #Initialize our dictionary
    posts = {}

    #We know the format
    for i in range(0,len(lines),12):
        data = [lines[i+j].strip().split(":")[1] for j in range(1,11)]
        data[5] = data[5].split(",")
        p = PiazzaPost(data)
        posts[str(i/12)] = p
    return posts

if __name__=='__main__':
  posts = readPiazzaData("piazzaData.txt")
  print posts["3422"]
  #This is test code that should run the first time you run "python indexer.py"
  #Expected output is (not including the triple quotes):
  """
---------------------------------------------------------------------------------
Piazza Post: 3422
Poster: instructor
Num Views: None
Type: i_answer
Created: 2014-10-15T18
Tags: 
Endorsements: 1
Response To: 3421
Subject: 
Content: Please include the question itself when posting about CodeLab (as stated in @6). As for the feedback, it usually gives you examples that CodeLab runs, listing what your result was and what the final result should have been. In terms of corner cases, some possibilities to think about are
--------------------------------------------------------------------------------
  """
