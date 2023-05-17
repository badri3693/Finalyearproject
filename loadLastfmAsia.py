import random 
import pymetis
import csv


def loadgraph():
    n = 7624
    Graph = []
    for i in range(n):
        Graph.append({})
    file1 = open("lastfm_asia_edges.csv","r")
    csvreader = csv.reader(file1)
    for row in csvreader:
        a,b = [int(k) for k in row]
        weight = random.randint(1,10)
        Graph[a][b] = weight
        Graph[b][a] = weight

    file1.close()
    return Graph

def membership(k):
    n = 7624
    Graph = []
    for i in range(n):
        Graph.append([])
    file1 = open("lastfm_asia_edges.csv","r")
    csvreader = csv.reader(file1)
    for row in csvreader:
        a,b = [int(k) for k in row]
        Graph[a].append(b)
        Graph[b].append(a)
    file1.close()
    membership = []
    for i in range(1,k , 4):
        n_cuts, membership_ = pymetis.part_graph(i, adjacency=Graph)
        membership.append(membership_)
    return membership