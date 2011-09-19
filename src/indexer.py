'''
Created on 14.09.2011
The indexer filters textdocuments for wordstems
and returns everything as a dict()
@author: kq
'''

from json import load
from re import finditer, compile
import string
from stemming.porter2 import stem
from hashlib import sha512, sha256
import uuid

class indexer(object):
    def __init__(self):
        self.stopwords = open("stopwords.lst", "r")
        self.stopwordsList = set(load(self.stopwords))
        self.to_index = open("text.txt", "r")
        self.pattern = compile(r"[a-zA-Z0-9]{2,35}")

    # Check our Textdocument with our regex (self.pattern)
    def check_document(self, document=open("text.txt", 'r')):
        try:
            # init some vars we need
            words = 0
            out = list()
            
            # for every match we find with our regex
            for match in finditer(self.pattern, document.read()):
                # increment words with itself plus one and append the 
                # lowercase representation of the string to our list
                words = words + 1
                out.append(string.lower(match.group(0)))
            return {'wordcounter' : words, 'words' : set(out)}
        
        except ValueError as msg:
            print "ValueError: " + str(msg) + "\n"

        finally:
            print "Finished checking document (" + str(document.name) + ").."
            document.close()
    
    # This function removes every stopword (words we don't need to index 'cuz they are not necessary for searchquerys)
    def remove_stopwords(self, lst):
        wordlist = lst
        try:
            delCounter = 0
            for stopword in self.stopwordsList:
                if stopword in wordlist:
                    delCounter = delCounter +1
                    lst.remove(stopword)
            return  {'deleted' : delCounter, 'words' : lst}

        except ValueError as msg:
            print "ValueError: " + str(msg) + "\n"
        
        finally:
            print "Finished removing all stopwords.."

    # Guess what it does.
    def word_stemmer(self, lst):
        cnt = 0
        try:
            word_set = set(lst)
            out = list()
            for item in word_set:
                cnt = cnt + 1
                out.append(stem(item))
            return set(out)

        except Exception as msg:
            print msg
        
        finally:
            print "Stemming finished\nWords left\t[" + str(cnt) + "]"
    
    def create_unique_docID(self, docpath):
        docID = str(uuid.uuid1())
        return {
                'uuid' : docID,
                'path' : docpath
                }