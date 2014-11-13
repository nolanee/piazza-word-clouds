import re

class PiazzaPost(object):

    #Default constructor for a PiazzaPost object
    def __init__(self):
        self.id = ""
        self.poster = ""
        self.numViews = None
        self.type = None
        self.created = ""
        self.tags = None
        self.endorsements = 0
        self.responseTo = ""
        self.subject = None
        self.content = None

    #Nondefault constructor for a PiazzaPost object
    def __init__(self,info):
        self.id = info[0]
        self.poster = info[1]
        self.numViews = info[2]
        self.type = info[3]
        self.created = info[4]
        self.tags = info[5]
        self.endorsements = info[6]
        self.responseTo = info[7]
        self.subject = info[8]
        self.content = info[9]

    #Function that allows you to just call print on an instance
    #p = PiazzaPost()
    #print p
    def __str__(self):
        s = "-"*80
        s += "Piazza Post: "+str(self.id)+"\n"
        s += "Poster: "+self.poster+"\n"
        s += "Num Views: "+self.stringNone(self.numViews)+"\n"
        s += "Type: "+self.stringNone(self.type)+"\n"
        s += "Created: "+self.created+"\n"
        s += "Tags: "+", ".join(self.stringNone(self.tags))+"\n"
        s += "Endorsements: "+str(self.endorsements)+"\n"
        s += "Response To: "+str(self.responseTo)+"\n"
        s += "Subject: "+self.stringNone(self.subject)+"\n"
        s += "Content: "+self.stringNone(self.content)+"\n"
        s += "-"*80
        return s

    #Helper function for __str__() that deals with null (None) values
    def stringNone(self,val):
        if val == None:
            return "None"
        return val
