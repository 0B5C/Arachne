'''
Make chunks from a dictionary and send it to cassandra
Created on 24.09.2011

@author: kq
'''
import db_communication

class chunksys(object):
    # chunks should be a iterable list
    # determine how many chunks are inside, if 
    # there is more than 3 chunks push everything to a
    # local cassandradatabase to prevent bigger data loss
    def storagePersistor(self, chunks):
        # TODO: Create db_connection multiset for local use
        try:
            if len(chunks) > 3:
                db = db_communication.db_com()
                for item in chunks:
                    db.localMultiset(item)
                return 0

        except Exception as msg:
            # TODO: Exceptionhandler
            print str(msg)
            return -1


    def createChunk(self, inputDictionary, count, isLast=False):
        try:
            if count == 10 or isLast == True or len(str(inputDictionary)) >= 15728640:
                if inputDictionary != None:
                    return inputDictionary

        except Exception as msg:
            print str(msg)

    #chunks should be an iterable list of dictionarys
    def transfer(self, chunkstorage):
        try:
            db = db_communication.db_com()
            # push self.chunks to cassandra
            for item in chunkstorage:
                res = db.multi_set_words(item)
            if res == -1:
                print "Error, could not push to cassandra."
                if res == -1:
                    print "[FAILED] - Chunks were not pushed to cassandra."
                return -1
            return 0

        except Exception as msg:
            print str(msg)