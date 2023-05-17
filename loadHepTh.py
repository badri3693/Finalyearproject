import random 
import pymetis


def loadgraph():
    n = 9877
    Graph = []
    for i in range(n):
        Graph.append({})
    file1 = open("CA-HepTh.txt","r")
    for i in range(4):
        file1.readline()
    while True:
        line = file1.readline().strip("\n").split("\t")
        if(line[0]==''):
            break
        try:
            a = int(line[0])
        except:
            print(line[0])
        b = int(line[1])
        if ( a>=9877 or b >= 9877 ):
            continue
        weight = random.randint(1,10)
        Graph[a][b] = weight
        Graph[b][a] = weight

    file1.close()
    return Graph

def membership(k):
    n = 9877
    Graph = []
    for i in range(n):
        Graph.append([])
    file1 = open("CA-HepTh.txt","r")
    for i in range(4):
        file1.readline()
    while True:
        line = file1.readline().strip("\n").split("\t")
        if(line[0]==''):
            break
        a = int(line[0])
        b = int(line[1])
        if ( a>=9877 or b >= 9877 ):
            continue
        Graph[a].append(b)
        Graph[b].append(a)
    file1.close()
    membership = []
    for i in range(1,k , 4):
        n_cuts, membership_ = pymetis.part_graph(i, adjacency=Graph)
        membership.append(membership_)
    return membership
