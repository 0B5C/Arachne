'''
This class crawls for files which are in 
a specified folder.

Created on 19.09.2011
@author: kq
'''

import dircache
from getpass import getuser as User
import sys

import indexer
import chunksys
import db_communication

class crawler(object):
    def __init__(self):
        self.index = indexer.indexer()
        self.database = db_communication.db_com()
        self.base_dir = ""
        self.store_me = dict()
        self.documentCount = 0 # Count the documents you crawled
        self.chunk = chunksys.chunksys()
        self.chunkstore = list()

    # Scans a folder for files
    # TODO: Only scan for .txt files
    def getFilelist(self, directory="/home/" + User() + "/test/small/"):
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
                if store_me.has_key(item) == True:
                    store_me[item][docID['uuid']] = ''
                    # store_me[item].update( { docID['uuid'] : '' })
                else:
                    store_me[item] = {docID['uuid'] : ''}
            self.documentCount += 1
            if self.documentCount == 10:
                self.documentCount = 0
                self.chunkstore.append(self.chunk.createChunk(store_me, self.documentCount))
            sys.stdout.write( "[-->]\t- Run "+str(i)+" of "+str(totalDocs)+" finished.\r")
            sys.stdout.flush()

        # be sure to send _all_ chunks:
        tmp_chunk = self.chunk.createChunk(store_me, self.documentCount, True)
        self.chunkstore.append(tmp_chunk)
        self.chunk.transfer(self.chunkstore)

        print "Finished indexing..\nSaving to cassandra.. This could take another while."
        print "\n\n[FINISH] - Terminating, dude."