'''
Created on 14.09.2011

@author: kq
'''
import indexer

def main():
    ind = indexer.indexer()
    regex_result = ind.check_document()
    print "Before:\t" + str(regex_result['wordcounter'])
    res = ind.remove_stopwords(regex_result['words'])
    print "After:\t" + str(regex_result['wordcounter'] - res['deleted'])
    
    for line in res['words']:
        print line

if __name__ == '__main__':
    main()