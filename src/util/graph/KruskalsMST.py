from src.util.graph.WeightedEdge import *

#/**
#* Kruskal's minimum spanning tree algorithm
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class KruskalsMST:
    
#/**
#* The ranks of the nodes
#*/
    #int[] ranks
    
#/**
#* The paths of the nodes
#*/
    #int[] paths
    def __init__(self):
        self.ranks = []
        self.paths = []
#/**
#* @see graph.GraphTransform#transform(graph.Graph)
#*/
    def transform(self, g):
        # This could be all messed up I'm not entirely sure what is being done here
#        WeightedEdge[] edges = (WeightedEdge[]) g.getEdges().toArray(new WeightedEdge[0]);
        #print "kruskals.transform.g.getEdges" + str(g.getEdges().__class__)
        edges = g.getEdges()
        print "Krusk.edges" + str(edges.__class__)
        #print "1kruskals.transform.edges" + str(edges[0])
 #       edges = [WeightedEdge(i) for i in edges]
        #print "2kruskals.transform.edges" + str(edges[0])
        #print "edges" + str(edges)
        edges.sort()
        for i in range(g.getNodeCount()):
            g.getNode(i).setEdges([])      
        
        self.ranks = [0] * g.getNodeCount()
        self.paths = [0] * g.getNodeCount()
        for i in range(g.getNodeCount()):
            self.ranks[i] = 0
            self.paths[i] = i
        
        for i in range(len(edges)):
            inx = edges[i].getA().getLabel()
            out = edges[i].getB().getLabel()
            if (self.set(inx) != self.set(out)):
                self.combine(inx, out)
                g.getNode(inx).connect(g.getNode(out), edges[i])
        self.ranks = None
        self.paths = None
        return g
    

#/**
#* Find the set label for a given index
#* @param i the set label to find
#* @return the root label of the set
#*/
    def set(self, i):
        if (self.paths[i] != i):
            self.paths[i] = self.set(self.paths[i])
        # }
        return self.paths[i]
    # }
    
#/**
#* Combine two the sets
#* @param i the first set to combine
#* @param j the second to combine
#*/
    def combine(self,i, j):
        self.link(self.set(i), self.set(j))
    
    
#/**
#* Link together two sets
#* @param i the first set
#* @param j the second set
#*/
    def link(self, i, j):
        if (self.ranks[i] > self.ranks[j]):
            self.paths[j] = i
        else:
            self.paths[i] = j
            if (self.ranks[i] == self.ranks[j]):
                self.ranks[j] = self.ranks[j] + 1
