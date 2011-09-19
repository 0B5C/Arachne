'''
Created on 14.09.2011
@author: kq
'''
import ConfigParser
from ConfigParser import NoOptionError

class config(object):
    
    def __init__(self):
        self.result = {
                       "server"     : None,         # Cassandra
                       "port"       : None,
                       "uname"      : None,
                       "password"   : None,
                       "indexerID"  : None,         # Look for unique ID
                       "to_index"   : None          # Crawler outputfile/database information
                       }

        self.cfg_path = "config.cfg"
        self.cfg_parser = ConfigParser.ConfigParser()
        self.cfg_parser.readfp(open(self.cfg_path, 'r'))
        
    def format_config(self, config_path="config.cfg"):
        # check if all sections are described, optional sections will be added
        # for debugging or userpurposes (more information like time taken etc.)
        if self.cfg_parser.has_section("database") == False or self.cfg_parser.has_section("indexer") == False:
            print "Error, sections missing. Check your configuration!"
            exit()
        
        try:
            self.result['server']   = self.cfg_parser.get("database", "server")
            print self.result
            self.result['port']     = self.cfg_parser.getint("database", "port")
            print self.result
            self.result['uname']    = self.cfg_parser.get("database", "uname")
            print self.result
            self.result['password'] = self.cfg_parser.get("database", "password")
            print self.result
            self.result['indexerID']= self.cfg_parser.get("indexer", "indexerID")
            print self.result
            self.result['to_index'] = self.cfg_parser.get("indexer", "to_index")
        
        except NoOptionError:
            print "Option is missing..."
            
        for key, value in self.result.items():
            print self.result[key]
            if self.result[key] == None:
                print str(key) + " " + str(value)
                print "Error in configurationfile, see key: " + str(key) + " value is " + str(value)
                exit()
        return self.result