import facebook
import numpy
from collections import Counter
from operator import itemgetter
from collections import OrderedDict
from flask import Flask
app = Flask(__name__)

#=====Put_Access_Token_Here=======================================
ACCESS_TOKEN = 'CAACEdEose0cBAJVY364jZBfk4ZA1DXVbgKoj2WoG2ZC2rrUTtcZBll3n4pt6QBxfBK8JGjq7IvRb8oOjLGTVNlqwnTnFs8rGNfUwsGy63g8zZCHiWn8XQdkTZB55Wz7zuHxwXKVV2qvgoATHLeTuutP7bTx71yAZBh9GILUlX2S4ICzmKMrCUaWWSvNJiWtvSvRHNy8Dip28wZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

#=====MainHtml====================================================
@app.route('/')
def index():
    needprint=''
    needprint+='<link href="http://www.flycan.com/flycancss/css_menu_01/002.css" rel="stylesheet" type="text/css" />'
    needprint+='<link rel="stylesheet" href="http://www.freewebsitetemplates.com/preview/beachresort/css/style.css" type="text/css">'
    needprint+='<link rel="stylesheet" href="http://www.freewebsitetemplates.com/preview/shared/previews.css" type="text/css">'
    needprint+= '<link rel="stylesheet" type="text/css" href="www.freewebsitetemplates.com/preview/shared/previews.css" />'
    needprint+='</head>'
    needprint+='<div id="templateInfo">'
    needprint+='<div>'
    needprint+='<h2><a target="_blank" href="/">&nbsp;<!-- Final Project Demo--></a></h2>'
    needprint+='<ul class="navigation">'
    needprint+='<li class="edit"><a rel="nofollow" href="/use/beachresort/" data-ga-event="click" data-ga-category="Previews Top Bar" data-ga-action="Ad Click" data-ga-label="Beach Resort">Facebook</a></li>'
    needprint+='<li class="download"><a href="/download/beachresort/" data-ga-event="click" data-ga-category="Previews Top Bar" data-ga-action="Download Click" data-ga-label="Beach Resort">API</a></li>'     
    needprint+='<li class="discuss"><a href="/discuss/beachresort/" data-ga-event="click" data-ga-category="Previews Top Bar" data-ga-action="Discuss Click" data-ga-label="Beach Resort">Develop</a></li>'    		     
    needprint+='</ul>'
    needprint+='</div>'
    needprint+='</div>'
    needprint+='<link href="http://www.flycan.com/flycancss/css_menu_01/002.css" rel="stylesheet" type="text/css" />'
    needprint+='<link rel="stylesheet" href="http://www.freewebsitetemplates.com/preview/beachresort/css/style.css" type="text/css">'
    needprint+='<link rel="stylesheet" href="http://www.freewebsitetemplates.com/preview/shared/previews.css" type="text/css">'
    needprint+= '<link rel="stylesheet" type="text/css" href="www.freewebsitetemplates.com/preview/shared/previews.css" />'
    needprint+='<div><h2>Final Project Demo</h2></div>'
    needprint+='<br>'
    needprint+='<li><a href="/feed_likes">Feed Likes Analysis</a><br><br><br></li>'
    needprint+='<li><a href="/photo_tags">Photo Tags Analysis</a><br><br><br></li>'
    needprint+='<li><a href="/starsign">Friend Starsign Analysis</a><br><br><br></li>'
    needprint+='<li><a href="/friend_gender">Friend Gender Analysis</a><br><br><br></li>'
    needprint+='<br><br><br><br><br><p1 style="background-color:blue;font-size:36px;font-family: impact;color:white;">Final Project Demo</p1>'
    needprint+='<div><img src="http://ext.pimg.tw/superven/1372095401-1275465833.png"  alt="Smiley face"></div>'
    
    return needprint
#=====Feed_likes_count============================================
@app.route('/feed_likes')
def feed_likes_count():
    needprint=''
    feeds = getFeeds(fb)
    feed_likes = getLikes(feeds,fb)
    list_id = calLikes(feed_likes)

    
    aftercount = OrderedDict(Counter(list_id).most_common())
    sorted(aftercount.items(), key=itemgetter(1))
    needprint += '<a href="/">Back To Main Page</a><br><br><br>'
    needprint += '============================<br>'
    needprint += 'Number of the latest feeds : %d<br>' % len(feeds)
    needprint += '============================<br>'
    for fbid in aftercount.keys():
        needprint += '%s : %d<br>' % (fbid, aftercount[fbid])
    needprint += '============================<br>'
    return needprint

def getFeeds(fb):
    print "start get Feeds"
    jsonFeeds = fb.get_connections('me','feed')['data']
    feeds = [(feed['id'], feed['created_time'],) for feed in jsonFeeds]
    return feeds

def getLikes(feeds,fb):
    print "start get Likes"
    feed_likes = {}
    for feed in feeds:
        feed_likes[feed[0]] = fb.get_connections(feed[0],'likes')['data']
    return feed_likes
    
def calLikes(feed_likes):
    print "start calculate LikesNum"
    list_id = []

    for fid in feed_likes.keys():
        for feed_like in feed_likes[fid]:
            tempstr = str(feed_like['name'].encode('utf-8'))
            list_id.extend(tempstr if type(tempstr) == list else [tempstr])
    return list_id
#=====Photos_Tags_count===========================================
@app.route('/photo_tags')
def photo_tags_count():
    needprint=''
    photos = getPhotos(fb)
    photo_tags = getTags(photos,fb)
    list_id = TagsNum(photo_tags)
    
    aftercount = OrderedDict(Counter(list_id).most_common())
    sorted(aftercount.items(), key=itemgetter(1))
    
    needprint += '<a href="/">Back To Main Page</a><br><br><br>'
    needprint += '============================<br>'
    needprint += 'Number of the latest photos : %d,<br>' % len(photos)
    needprint += '============================<br>'
    for fbid in aftercount.keys():
        needprint += '%s : %d<br>' % (fbid, aftercount[fbid])
    needprint += '============================<br>'
    return needprint

def getPhotos(fb):
    print "start get Photo"
    jsonFriends = fb.get_connections('me','photos')['data']
    photos = [(photo['id'],photo['created_time']) for photo in jsonFriends]
    return photos

def getTags(photos,fb): 
    print "start get Tags"
    photo_tags = {}
    for photo in photos:
        photo_tags[photo[0]] = fb.get_connections(photo[0],'tags')['data']
    return photo_tags

def TagsNum(photo_tags):
    print "start calculate TagsNum"
    list_id = []

    for pid in photo_tags.keys():
        for photo_tag in photo_tags[pid]:
            tempstr = str(photo_tag['name'].encode('utf-8'))
            list_id.extend(tempstr if type(tempstr) == list else [tempstr])
    return list_id

#=====Starsign_count==============================================
#friends_birthday
@app.route('/starsign')
def birthday_starsign_count():
    fbirths = getBirth(fb)
    return starsign(fbirths)

def getBirth(fb):
    print "start get birth"
    arg = {'fields': 'birthday,name'}
    fbirths = fb.get_object("me/friends",**arg)
    return fbirths

def starsign(fbirths):
    needprint=''
    name = []
    birth = []
    month=[]
    Aries=0 
    Taurus=0    
    Gemini=0
    Cancer=0    
    Leo=0   
    Virgo=0 
    Libra=0 
    Scorpio=0   
    Sagittarius=0   
    Capricorn=0 
    Aquarius=0  
    Pisces=0
    fri_bir=0
    for fbirth in fbirths['data']:
        if('birthday' in fbirth):
            tempstr = str(fbirth['birthday'])
            tempstr_c=tempstr.split("/")
            day =  int(str(tempstr_c[1]),10)
            month =  int(str(tempstr_c[0]),10)
            birth.extend(tempstr if type(tempstr) == list else [tempstr])
            fri_bir+=1
            if(month==1):
                if(day>=1 and day<=20):
                    Capricorn+=1
                else:
                    Aquarius+=1
            if(month==2):
                if(day>=1 and day<=29):
                    Aquarius+=1
                else:
                    Pisces+=1
            if(month==3):
                if(day>=1 and day<=20):
                    Pisces+=1
                else:
                    Aries+=1    
            if(month==4):
                if(day>=1 and day<=20):
                    Aries+=1
                else:
                    Taurus+=1
            if(month==5):
                if(day >=1 and day <=21):
                    Taurus+=1
                else:
                    Gemini+=1
            if(month==6):
                if(day >=1 and day <=21):
                    Gemini+=1
                else:
                    Cancer+=1
            if(month==7):
                if(day >=1 and day <=23):
                    Cancer+=1
                else:
                    Leo+=1
            if(month==8):
                if(day >=1 and day <=23):
                    Leo+=1
                else:
                    Virgo+=1
            if(month==9):
                if(day >=1 and day <=23):
                    Virgo+=1
                else:
                    Libra+=1
            if(month==10):
                if(day >=1 and day <=23):
                    Libra+=1
                else:
                    Scorpio+=1
            if(month==11):
                if(day >=1 and day <=22):
                    Scorpio+=1
                else:
                    Sagittarius+=1
            if(month==12):
                if(day >=1 and day <=22):
                    Sagittarius+=1
                else:
                     Capricorn+=1

    needprint += '<a href="/">Back To Main Page</a><br><br><br>'
    needprint += '============================<br>'
    needprint += 'Number of friends : %d<br>' % fri_bir
    needprint += '============================<br>'
    needprint += '%s : %d<br>' %("Aries",Aries)
    needprint += '%s : %d<br>' %("Taurus",Taurus)
    needprint += '%s : %d<br>' %("Gemini",Gemini)
    needprint += '%s : %d<br>' %("Cancer",Cancer)
    needprint += '%s : %d<br>' %("Leo",Leo)
    needprint += '%s : %d<br>' %("Virgo",Virgo)
    needprint += '%s : %d<br>' %("Libra",Libra)
    needprint += '%s : %d<br>' %("Scorpio",Scorpio)
    needprint += '%s : %d<br>' %("Sagittarius",Sagittarius)
    needprint += '%s : %d<br>' %("Capricorn",Capricorn)
    needprint += '%s : %d<br>' %("Aquarius",Aquarius)
    needprint += '%s : %d<br>' %("Pisces",Pisces)
    needprint += '============================<br>'

    return needprint

#=====Friend_Gender_count=========================================
#user_friends
@app.route('/friend_gender')
def friend_gender_count():
    return getFriends(fb)

def getFriends(fb):
    needprint=''
    print "start get friends"
    male=0
    female=0
    jsonFriends = fb.get_connections('me','friends', fields="gender")['data']
    for friend in jsonFriends:
        for key in friend.keys():
            if(friend[key]=='female'):
                female+=1
            if(friend[key]=='male'):
                male+=1

    needprint += '============================<br>'
    needprint += 'Number of friends : %d <br>' % len(jsonFriends)
    needprint += '============================<br>'
    needprint += 'Male : %d <br>' % (male)
    needprint += 'Female : %d <br>' % (female)
    needprint += '============================<br>'
    return needprint

#=====MainFunction================================================
if __name__ == '__main__':
    app.run()
