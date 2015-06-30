import facebook
import numpy
import networkx
import pylab
from collections import Counter
from operator import itemgetter
from collections import OrderedDict

G=networkx.Graph()

ACCESS_TOKEN = 'CAACEdEose0cBABeESASRzcKL4S6o0tFYBRxFpN3R1uIjitePYojWRrry1WAG4k3zJAz6ImcWPtfymRewKSRBruJF3aKNh6CL3Jk3h9cmRGZC8J8yk4nMh4bUNMxClMvaiofN5CqKnScKBNzeT4S1LWcoPWYkqh2oSYnPGl8UiIZBk8uPGstq9e5ZBddg86dkusyZBZB7rVgZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

def getFeeds(fb):
    print "start get feeds"
    jsonFeeds = fb.get_connections('me','feed')['data']
    feeds = [(feed['id'], feed['created_time'],) for feed in jsonFeeds]
#    print friends
    return feeds

def getLikes(feeds,fb):
    print "start get likes"
    feed_likes = {}
    for feed in feeds:
        feed_likes[feed[0]] = fb.get_connections(feed[0],'likes')['data']
#        print feed_likes[friend[0]]
    return feed_likes
    
def calLikes(feed_likes):
    print "start find big one"
    list_id = []

    for fid in feed_likes.keys():
        for feed_like in feed_likes[fid]:
            tempstr = str(feed_like['name'].encode('utf-8'))
            list_id.extend(tempstr if type(tempstr) == list else [tempstr])
    return list_id
    
#------------------------------------------------------------------------------------------
feeds = getFeeds(fb)
feed_likes = getLikes(feeds,fb)
list_id = calLikes(feed_likes)

print list_id
print '============================'

aftercount = OrderedDict(Counter(list_id).most_common())
sorted(aftercount.items(), key=itemgetter(1))

print 'Total new : %d' % len(feeds)
print '============================'
for fbid in aftercount.keys():
    print '%s : %d' % (fbid, aftercount[fbid])
print '============================'
print "finished!"
