'''
Created on 14.09.2011

@author: kq
'''
import indexer
import db_communication
from time import time

def main():
    start = time()
    ind = indexer.indexer()
    regex_result = ind.check_document()
    res = ind.remove_stopwords(regex_result['words'])
    sol = ind.word_stemmer(res['words'])

    docpath = "/home/kq/test.txt" # This should be the path to the document we indexed
    docID = ind.create_unique_docID(docpath)
    #create conform dict:
    store_me = dict()
    for item in sol:
        store_me[item] = { docID['uuid'] : '' }
    db = db_communication.db_com()
    db.multi_set_words(store_me)
    db.set_docID(docID)
    end = time()
    
    print str(end - start)

if __name__ == '__main__':
    main()