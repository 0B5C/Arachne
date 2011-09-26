'''
Created on 14.09.2011
@author: kq
'''
import ConfigParser
from ConfigParser import NoOptionError

class config(object):
    # TODO: Add option for which directory should be monitored
    def __init__(self):
        self.cfg_path = "config.cfg"
        self.cfg_parser = ConfigParser.ConfigParser()
        self.cfg_parser.readfp(open(self.cfg_path, 'r'))

    def format_config(self, config_path="config.cfg"):
        # check if all sections are described, optional sections will be added
        # for debugging or userpurposes (more information like time taken etc.)
        if self.cfg_parser.has_section("database") == False or self.cfg_parser.has_section("indexer") == False:
            print "Error, sections missing. Check your configuration!"
            exit()
        
        result = {}

        try:
            result['server']   = self.cfg_parser.get("database", "server")
            result['port']     = self.cfg_parser.getint("database", "port")
            result['uname']    = self.cfg_parser.get("database", "uname")
            result['password'] = self.cfg_parser.get("database", "password")
            result['indexerID']= self.cfg_parser.get("indexer", "indexerID")
            result['to_index'] = self.cfg_parser.get("indexer", "to_index")
        
        except NoOptionError:
            print "Option is missing..."
            
        return result