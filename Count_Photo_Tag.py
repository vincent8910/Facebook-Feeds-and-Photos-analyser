import facebook
import pylab
from collections import Counter
from operator import itemgetter
from collections import OrderedDict

ACCESS_TOKEN = 'CAACEdEose0cBAMbw4auFwq8UJ8fna5jb2wrZB7QoZC02CWQNECBIgsvltAy6OgR40ZCXgJQZCfUX4MetUKrT8ZBmIyqXaRcUbvQcU3DIPAjzTyR4uSdjo3YvzSkJrlJD07uwReoWhUqIN40YoPBhwbDNiFAzcZCxTSS9i48zJZA1ATBPFwqyKXY8DNBbDvJ7dHzjZAtS1SNhJwZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

def getPhotos(fb):
    print "start get Photo"
    jsonFriends = fb.get_connections('me','photos')['data']
    photos = [(photo['id'],photo['created_time']) for photo in jsonFriends]
    print photos
    return photos

def getTags(photos,fb): #得到所tag的user他們的一些欄位資料,如 id,name,created time....
    print "start get Tags"
    photo_tags = {}
    for photo in photos:
        photo_tags[photo[0]] = fb.get_connections(photo[0],'tags')['data']
        print photo_tags[photo[0]]
    return photo_tags

def TagsNum(photo_tags):#把這些照片中有tag到的人都存到陣列list_id,人名若重複則照樣存入
    print "start calculate TagsNum"
    list_id = []

    for pid in photo_tags.keys():
        for photo_tag in photo_tags[pid]:
            tempstr = str(photo_tag['name'].encode('utf-8'))
            list_id.extend(tempstr if type(tempstr) == list else [tempstr])
    return list_id
#------------------------------------------------------------------------------------------
photos = getPhotos(fb)
photo_tags = getTags(photos,fb)
list_id = TagsNum(photo_tags)

print list_id
aftercount = OrderedDict(Counter(list_id).most_common())
sorted(aftercount.items(), key=itemgetter(1))

print '============================'
print 'Number of the latest photos : %d' % len(photos)
print '============================'
for fbid in aftercount.keys():
    print '%s : %d' % (fbid, aftercount[fbid])
print '============================'

print "finished!"
