'''
The whole database work is done here
Created on 19.09.2011
@author: kq
'''
import pycassa

import config
# TODO: Exceptionhandling
class db_com(object):

    # TODO: Read from config
    def __init__(self):
        cfg = config.config().format_config()
        self.pool = pycassa.connect('indexer', [str(cfg['server']) + ':' + str(cfg['port'])])
        self.col_fam_name = 'indexx'
        self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)

    '''
    # @DEPRECATED:
    The dictionary you throw into this should look like:
    {
    'word0' : {'docID-00' : ''},
    'word1' : {'docID-01' : ''}
    }
    
    This is just a standard, if a word occurs in more than one doc do something like that:
    {
    'word0' : {
                'docID-00' : '',
                'docID-01' : ''
              },
    'word1' : {'docID-01' : ''}
    }
    '''
    
    def localMultiset(self, chunks):
        if chunks == None:
            return

        if self.col_fam_name != 'local_indexx':
            self.col_fam_name = 'local_index'
            self.pool = pycassa.connect('local_index', ['localhost:9160'])
            self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)
        # TODO: Datenbank beibringen ueber listen zu iterieren

        try:
            self.col_fam.batch_insert(chunks)
            return 0

        except Exception as msg:
            print str(msg)
            return -1


    def multi_set_words(self, indexer_resultset):
        if indexer_resultset == None:
            return

        if self.col_fam_name != 'indexx':
            self.col_fam_name = 'indexx'
            self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)

        try:
            self.col_fam.batch_insert(indexer_resultset)
            return 0

        except Exception as msg:
            print "[ERROR] - " + str(msg)
            return -1

    # The set_docID function saves a docID into our database (CF: docids)
    def set_docID(self, docID_dict):
        if docID_dict == None:
            return

        if self.col_fam_name != 'docids':
            self.col_fam_name = 'docids'
            self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)

        try:
            self.col_fam.insert(docID_dict['uuid'], {'path' : docID_dict['path']})
            return 0
        except Exception as msg:
            print "[ERROR] - " + str(msg)
            return -1