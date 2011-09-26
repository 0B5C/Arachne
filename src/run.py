'''
This is our main function which executes the crawler
Created on 14.09.2011
@author: kq
'''
from time import time
import crawler
def main():
    print '''
                            .__                   
 _____ ____________    ____ |  |__   ____   ____  
 \__  \\_  __ \__  \ _/ ___\|  |  \ /    \_/ __ \ 
  / __ \|  | \// __ \\  \___|   Y  \   |  \  ___/ 
 (____  /__|  (____  /\___  >___|  /___|  /\___  >
      \/           \/     \/     \/     \/     \/ 
v0.1 -                Kai Oliver Quambusch / 2011
    '''
    inp = raw_input("-Press the Anykey to start-")
    print inp
    crawl = crawler.crawler()
    crawl.__init__()
    start = time()
    filelist = crawl.getFilelist()
    crawl.crawlFilelist(filelist)
    end = time()

    print "[FINISH] - " + str(end - start) +"s"

if __name__ == '__main__':
    main()