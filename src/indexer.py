'''
Created on 14.09.2011
The indexer filters textdocuments for wordstems
and returns everything as a dict()
@author: kq
'''

from json import load
from re import finditer, compile
from stemming.porter2 import stem
import uuid
from time import time

class indexer(object):
    def __init__(self):
        self.stopwords = open("stopwords.lst", "r")
        self.stopwordsList = set(load(self.stopwords))
        self.pattern = compile(r"[\b\w\b]{2,35}")
        self.totalT = float()

    # Check our Textdocument with our regex (self.pattern)
    def check_document(self, document=open("text.txt", 'r')):
        if self.totalT != 0.0:
            self.totalT = 0.0
        s = time()
        try:
            
            # init some vars we need
            out = set()
            
            # for every match we find with our regex
            for match in finditer(self.pattern, document.read()):
                # increment words with itself plus one and append the 
                # lowercase representation of the string to our list
                out.add(match.group(0).lower())
            return {'words' : out}
        
        except ValueError as msg:
            print "ValueError: " + str(msg) + "\n"

        finally:
            en = time() - s
            #print "[--Run--]\t- checking document (" + str(document.name) + ")\t[" + str(en) + "s]"
            self.totalT = self.totalT + en
            document.close()

    # This function removes every stopword (words we don't need to index 'cuz they are not necessary for searchquerys)
    def remove_stopwords(self, lst):
        s = time()
        wordlist = lst
        try:
            for stopword in self.stopwordsList:
                if stopword in wordlist:
                    lst.remove(stopword)
            return  {'words' : set(lst)}

        except ValueError as msg:
            print "ValueError: " + str(msg) + "\n"

        finally:
            en = time() - s
            #print "[--Run--]\t- Removing stopwords\t\t\t\t[" + str(en) + "s]"
            self.totalT = self.totalT + en

    # Guess what it does.
    # todo ask for type and cast to set if this is a list
    def word_stemmer(self, lst):
        s = time()
        try:
            word_set = set(lst)
            out = set()
            for item in word_set:
                out.add(stem(item))
            return out

        except Exception as msg:
            print msg

        finally:
            en = time() - s
            #print "[--Run--]\t- Stemming words\t\t\t\t[" + str(en) + "s]"
            self.totalT = self.totalT + en
            #print "TOTAL: " + str(self.totalT) + "\b",

    def create_unique_docID(self, docpath):
        docID = str(uuid.uuid1())
        return {'uuid' : docID, 'path' : docpath}
