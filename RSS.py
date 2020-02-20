import feedparser
from time import mktime
from datetime import datetime
url = 'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml'
feed = feedparser.parse(url)
link = open('C:\\Users\\elnaz\\Desktop\\link.txt','w')
published_date = open('C:\\Users\\elnaz\Desktop\\publish.txt','w')
title = open('C:\\Users\\elnaz\\Desktop\\title.txt','w')
description = open('C:\\Users\\elnaz\\Desktop\\descr.txt','w')
count =1
for post in feed.entries:
   ttle = post.title
   title.write(str(count) + "\n")
   dt = post.published
   description.write(str(count) + "\n")
   link.write(str(count) + "\n")
   published_date.write(str(count) + "\n")
   ll = post.link
   FEED_DATE = (post.updated_parsed)
   des = post.description
   title.write(str(ttle.encode('utf-8','ignore')) + "\n")
   link.write(ll.encode('utf-8','ignore') + "\n")
   description.write(str(des.encode('utf-8','ignore')) + "\n")
   published_date.write(str(dt.encode('utf-8','ignore')) + "\n")
   count+=1
title.close()
description.close()
link.close()
published_date.close()
