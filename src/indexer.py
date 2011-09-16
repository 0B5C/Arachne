'''
Created on 14.09.2011

@author: kq
'''
import json
import re
import string

class indexer(object):
    def __init__(self):
        self.stopwords = open("stopwords.lst", "r")
        self.stopwordsList = set(json.load(self.stopwords))
        self.to_index = open("text.txt", "r")
        self.pattern = re.compile(r"[a-zA-Z0-9]{2,35}") 
        
        # TODO: GOOGLE> Stream parser
        
    def check_document(self, document=open("text.txt", 'r')):
        try:
            words = 0
            out = list()
            for match in re.finditer(self.pattern, document.read()):
                words = words + 1
                out.append(string.lower(match.group(0)))
            return {'wordcounter' : words, 'words' : set(out)}
        
        except ValueError as msg:
            print "ValueError: " + str(msg)
        
        finally:
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
            print "\nSomething, somewhere went terrible wrong.\nValueError: " + str(msg) + "\n"
    
    def word_stemmer(self, document_as_list):
        pass