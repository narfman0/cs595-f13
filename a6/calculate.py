#!/usr/bin/python3
import igraph
import sys

DEFAULT_FILE='karate.net'
if len(sys.argv) != 2:
        print('Pass the path to your graph file, defaulting to '+DEFAULT_FILE)
        path=DEFAULT_FILE
else:
        path=sys.argv[1]

for x in range(2, 6):
    k = igraph.load(path)
    vertexDendrogram = k.community_edge_betweenness(clusters=x, directed=False)
    vertexClustering = vertexDendrogram.as_clustering()
    print('Modularity: ' + str(vertexClustering.modularity))
    print(vertexClustering)
    i=0
    for subgraph in vertexClustering.subgraphs():
        subgraph.save(str(x)+'-karate-'+str(i)+'.svg', format="svg")
        i+=1
