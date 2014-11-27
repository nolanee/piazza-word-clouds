piazzaWordClouds
================

This README mostly just has examples and special cases to be aware of.
For actual project instructions, see the spec.

indexer.py
==========

general comment - indexer.py is actually a class we have defined in Python.
                  Because of this, it has some components you may not be
                  familiar with. One good example is the __init__() thing, 
                  which is a constructor. You don't need to change it.
                - The important thing about it being a function is this:
                  if you want to make new functions, they MUST have 'self'
                  as the first argument. Look at any of the starter functions
                  for an example

__init__ - This is a Python constructor. You do NOT need to alter this for
           the core. It's just here so that we can use our object in
           visualizer.py.

removePunctuation - The following symbols are considered punctuation:

                    !@#$%^&*()-_+=~`{}|[]\:";'<>?,./

                  - NOTE: If you are doing a Reach component that requires you
                          track these symbols, you must do so ONLY for the
                          Showcase. Do NOT including counts for these symbols
                          in your Core implementation EVEN IF they are part of
                          your Reach.

tokenize - The following symbols are considered whitespace:

           " ", "\t", "\n", "\r", "\f", "\v"

         - Here are two examples. The second one is tricky.
             1. "hello reed" -> ["hello", "reed"]
             2. "hello \t\nshibu" -> ["hello", "shibu"]

readPiazzaData() - You do NOT need to change this function for the core!


visualizer.py
=============

binPiazzaPosts - For the core, we will be binning posts by week.
                 You MAY need to change this function for your Reach code.
                 Submit the UNCHANGED version for the core

drawWordCloud - We are not actually grading your word clouds for the core
                We ARE grading your singleBinDictionary, though
                Also, you will need this function for the showcase, so it's
                in your best interest to put some effort in to it.
                There is a small portion of your showcase grade for how nice
                your word clouds look. It's very subjective, so as long as it's
                clear you put effort in you'll get full points for that.

drawTimeLine - drawTimeLine is sort of the workhorse of this file.
               It is in charge of getting the separate word clouds created
               as well as assembling them into one timeline. This function
               should return ONE surface, which main() will interact with
               to produce the actual timeline sensation. A quick example is
               below but a fuller example will be added to the spec soon.

          Week 2
             |
             v                               The idea is that drawTimeLine just
----------------------------etc.             returns this sort of picture.
  ^                     ^                    Main() will then make some
  |                     |                    alterations in a loop to highlight
Week 1               Week 3                  particular weeks.

              You may make any alterations you wish, and we are only grading
              the looks at the Showcase. For the core, so long as there is
              *some* kind of highlighting in a loop, we will be happy. It's
              also fine if they are not all visible at the same time.
                

dummyIndex - Just a function that we added to make sure you can work on
             visualizer.py easily before indexer.py is finished. It just
             makes a fake index in (almost) the correct format.
             You should be able to use it to get most of the bigger functions
             going even though the real result of indexer will be slightly
             different (Dictionary of piazzaPost objects, not strings)

main - main does two things: 1. Make an indexer object that does all the
                                necessary calculations
                             2. Use the resulting tfidf dictionary to draw
                                the timeline.

     - In order for you to be able to work on the visualization before the
       indexer is finished, I have included the dummyIndex() function.
       This is ONLY for testing before you have finished indexer, to allow
       you to split up the work more easily/efficiently.
