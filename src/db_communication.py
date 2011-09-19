import pycassa

class db_com(object):
    def __init__(self):
        self.pool = pycassa.connect('indexer', ['localhost:9160'])
        self.col_fam_name = 'indexx'
        self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)

    def set(self, word, documentID):
        if self.col_fam_name != 'indexx':
            self.col_fam_name = 'indexx'
        try:
            self.col_fam.insert(word, {documentID : ''})
            return 0
        
        except Exception as msg:
            print msg
            return -1

    '''
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
    def multi_set_words(self, indexer_resultset):
        if self.col_fam_name != 'indexx':
            self.col_fam_name = 'indexx'
            self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)
            print self.col_fam_name

        try:
            self.col_fam.batch_insert(indexer_resultset)
            return 0
        
        except Exception as msg:
            print msg
            return -1
    
    def set_docID(self, docID_dict):
        if self.col_fam_name != 'docids':
            self.col_fam_name = 'docids'
            self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)
            print self.col_fam_name

        try:
            self.col_fam.insert(docID_dict['uuid'], {'path' : docID_dict['path']})
            return 0
        except Exception as msg:
            print msg
            return 1

    def get(self, key):
        pass