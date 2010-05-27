import feedparser
import re
FEED_URL= "http://screencasters.heathenx.org/feed/"
RUTA = "http://screencasters.heathenx.org/wp-content/videos/ep"

feed = feedparser.parse(FEED_URL)

last_post = feed.entries[0]
last_ep_number = re.search('\d{2,3}', last_post.title).group(0)
print int(last_ep_number)
for i in range(1, int(last_ep_number)):
    ep_number = str(i)
    if len(ep_number)==2:
        ep_number = '0' + ep_number
    elif len(ep_number)==1:
        ep_number = '00' + ep_number

    print 'wget -c %s%s.ogv' % (RUTA, ep_number) 
