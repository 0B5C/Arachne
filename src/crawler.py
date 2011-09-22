'''
This class crawls for files which are in 
a specified folder.

Created on 19.09.2011
@author: kq
'''

import dircache
import indexer
import db_communication
import sys

class crawler(object):
    def __init__(self):
        self.index = indexer.indexer()
        self.database = db_communication.db_com()
        self.base_dir = ""

    # Scans a folder for files
    # TODO: Only scan for .txt files
    def getFilelist(self, directory="/home/kq/test/"):
        self.base_dir = directory
        return dircache.listdir(directory)

    # do getFilelist and submit list here:
    def crawlFilelist(self, files):
        print "Indexing, this could take a while.."
        i = 0
        totalDocs = len(files)
        store_me = dict()
        for item in files:
            i = i + 1
            # create a unique docID (check on server if docID is already in use, 
            # if yes generate new one
            docID = self.index.create_unique_docID(self.base_dir + item)
            # check document, remove all stopwords and stem words
            res = self.index.check_document(open(self.base_dir + item, 'r'))
            res = self.index.remove_stopwords(res['words'])
            res = self.index.word_stemmer(res['words'])
            # save docID to database
            self.database.set_docID(docID)
            
            # create dictionary which contains all wordstems
            # should look like this:
            # {wordstem : { docID : '' }}
            for item in res:
                store_me[item] = { docID['uuid'] : '' }
            sys.stdout.write( "[-->]\t- Run "+str(i)+" finished of "+str(totalDocs)+"\r")
            sys.stdout.flush()
        print "Finished indexing..\nSaving to cassandra.. This could take another while."
        self.database.multi_set_words(store_me)
        print "\n\n[FINISH] - Terminating, dude."