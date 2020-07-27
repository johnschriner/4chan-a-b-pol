from bs4 import BeautifulSoup, NavigableString
import urllib2
import sys
import re
import time
from HTMLParser import HTMLParser
import htmlentitydefs
#if __name__ == "__main__":
#    reload(sys)
#    sys.setdefaultencoding("utf-8")

sys.setrecursionlimit(2000)

#using beautiful soup
f = open("2019-output.txt","a") 
p = open("2019b.txt","r")
p = p.read()
#print p
#print "done"

#p = str(p).replace('<blockquote class="postMessage" ',' ')
#p = str(p).replace('<a data-cmd="embed" data-type="yt" href="javascript:;">Embed</a>',' ')
p = str(p).replace('</blockquote>, ',' ')
#p = str(p).replace('<span class="quote">&gt;',' ')
#p = str(p).replace('</span>',' ')
#p = str(p).replace('<s>',' ')
#p = str(p).replace('</s>',' ')
p = str(p).replace('<br>',' ')
p = str(p).replace('<br/>',' ')
p = str(p).replace('</wbr>',' ')
p = str(p).replace('<wbr>',' ')

#p = re.sub(ur' id=.............',' ', p)

f.write(str(p))
f.close()
