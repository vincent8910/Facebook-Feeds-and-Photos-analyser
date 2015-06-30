import facebook
import numpy

ACCESS_TOKEN = 'CAACEdEose0cBAAqANF6xoYmZAQ2xkjrfFqAa8YV2JvW9jlQgNS3C9OvkUyvZC9Q8xhmY8NDsyqLZBRyoMzSFRReNyYHKhi79YnfK7Tl7hEVOJcTl9KzR5KKQXhVjMJPGjjOQB7IC9soItekJThZBDR0vhLnN0aczWSIN5lBYpFZC23Lk4Oumnudw9R7ItsfE7NPRjIV0B0gZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

def getFriends(fb):
    print "start get friends"
    male=0
    female=0

    jsonFriends = fb.get_connections('me','friends', fields="name,gender")['data']
    #get friends(array of user-object), and need a fields names 'gender'
    for friend in jsonFriends:
    #get each friend object
        for key in friend.keys():
        #get each attribute, we can't use 'gender', so waste some time to use run every attribute
            if(friend[key]=='female'):
                female+=1
            if(friend[key]=='male'):
                male+=1

    print female
    print male
    return 0
    
#------------------------------------------------------------------------------------------
friends = getFriends(fb)

print "finished!"
