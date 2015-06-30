import facebook
import numpy
import networkx
import pylab

G=networkx.Graph()

ACCESS_TOKEN = 'CAACEdEose0cBADMtYXTckeVYI07D5NoFZCzakOZCzc820r0H5BntJJUAUWkxkXvuvnwapIHYw2jRZAva7fs32q6qPeLSmjRnFGkVkvQ6AZBlRN9CS7QcGGDCWsNLUqplNJF0vjK3D0EwTLkTn6abNVY2qhXA5O1LaHRHk8jSxFumXStJTWndSqs4dbZA9tXUogjHUNOPiQwZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

def getFriends(fb):
    print "start get friends"
    jsonFriends = fb.get_connections('me','friends')['data']
    friends = [(friend['id'], friend['name'],) for friend in jsonFriends]
#    print friends
    return friends

def getFriendIndex(friends):
    print "start get friend_index"
    friend_index = {}
    for i in range(0,len(friends),1):
        friend_index[friends[i][0]] = [i,friends[i][0],friends[i][1]]
#    print friend_index
    return friend_index

def getMutualFriends(friends,fb):
    print "start get mutual_friends"
    mutual_friends = {}
    for friend in friends:
        mutual_friends[friend[0]] = fb.get_connections(friend[0],'mutualfriends')['data']
#        print mutual_friends[friend[0]]
    return mutual_friends
    
def getAdjacency_matrix(mutual_friends,friend_index):
    print "start get Adjacency_matrix"
    adjacency_matrix=numpy.zeros([len(friend_index),len(friend_index)])
    for fid in mutual_friends.keys():
        for mutual_friend in mutual_friends[fid]:
            x = friend_index[fid][0]
            y = friend_index[mutual_friend['id']][0]
            adjacency_matrix[x,y]=1
            G.add_edge(x,y)
    return adjacency_matrix

def write_friend_index(friend_index,path):
    f = open(path,'wb')
    for key in friend_index.keys():
        f.write(str(friend_index[key][0]) + "," + friend_index[key][2].encode('utf-8') + "\n")
    f.close()

def wirte_degree_centrality(adjacency_matrix,path):
    f = open(path, 'wb')
    drgreelist=numpy.zeros([len(adjacency_matrix[0])])
    for all in range(0,len(adjacency_matrix[0])-1):
        drgreelist[all]=sum(adjacency_matrix[all])
        f.write(str(all)+","+str(drgreelist[all])+"\n")
    f.close()
    
#------------------------------------------------------------------------------------------

friends = getFriends(fb)

friend_index = getFriendIndex(friends)

mutual_friends = getMutualFriends(friends,fb)

adjacency_matrix = getAdjacency_matrix(mutual_friends,friend_index)

write_friend_index(friend_index,'friend_index.csv')

numpy.savetxt("adjacency_matrix.csv", adjacency_matrix , fmt='%d' , delimiter=",")

wirte_degree_centrality(adjacency_matrix,'degree.csv')

networkx.draw(G)

pylab.savefig('test.png')

pylab.show()

print len(friends)

print "finished!"
