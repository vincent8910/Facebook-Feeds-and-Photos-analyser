import numpy
import networkx
import pylab

g=networkx.Graph()
data=numpy.array([
    [0,1,1,1,0,0,0,0],
    [1,0,0,1,1,0,0,0],
    [1,0,0,0,0,1,1,1],
    [1,1,0,0,1,0,0,0],
    [0,1,0,1,0,0,0,0],
    [0,0,1,0,0,0,1,0],
    [0,0,1,0,0,1,0,1],
    [0,0,1,0,0,0,1,0]
    ])


x=1
for i in data:
    y=1
    for j in i:
        if(j==1):
            print x,y
            g.add_edge(x,y)
        y+=1
    x+=1
    
networkx.draw(g)

pylab.savefig('test.png')

degree_centrality = networkx.degree_centrality(g)

print degree_centrality
print degree_centrality.keys()
print [degree_centrality[x] for x in degree_centrality.keys()]
print degree_centrality[1]
print degree_centrality[7]

print 'OK'