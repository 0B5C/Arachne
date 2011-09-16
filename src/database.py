'''
Created on 14.09.2011

@author: kq
'''
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from cassandra import Cassandra
from cassandra.ttypes import *
import time
import pprint

class Database(object):
    def __init__(self):
        self.socket = TSocket.TSocket("localhost", 9160)
        self.transport = TTransport.TBufferedTransport(self.socket)
        self.protocol = TBinaryProtocol.TBinaryProtocolAccelerated(self.transport)
        self.client = Cassandra.Client(self.protocol)
        
        self.pp = pprint.PrettyPrinter(indent=2)
    
    # Params we need in our functions:
    # keyspace, key, value, timestamp
    
    # NOTE: Name durch Columnobjekt ersetzen
    def exec_insert(self, key="", name="", keyspace="indexer", column_fam="indexx"):
        try:
            timestamp = time.time()
            self.transport.open()
            insert_me = Column(name, "", timestamp)
            insertBlock = {
                           'indexx' : [
                                       ColumnOrSuperColumn(column=insert_me, super_column=None, counter_column=1, counter_super_column=0)
                                       ]
                           }

            for item in key:
                map = {
                       item : insertBlock
                       }
            self.client.batch_mutate(map, ConsistencyLevel.ANY)
        except Thrift.TException, tx:
            print "Thrift: %s" % tx.message
