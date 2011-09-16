'''
Created on 14.09.2011

@author: kq
'''
import indexer
from time import time

def main():
    ind = indexer.indexer()
    t_regex_start = time()
    regex_result = ind.check_document()
    t_regex_end = time()
    print "RegEx:\t\t" + str(t_regex_end - t_regex_start) + " seconds"
    print "Before:\t" + str(regex_result['wordcounter'])
    t_rem_start = time()
    res = ind.remove_stopwords(regex_result['words'])
    t_rem_end = time()
    print "Removing:\t" + str(t_rem_end - t_rem_start) + " seconds"
    print "After:\t" + str(regex_result['wordcounter'] - res['deleted'])
    print "Stemming in progress.."
    sol = ind.word_stemmer(res['words'])
    print sol

if __name__ == '__main__':
    main()