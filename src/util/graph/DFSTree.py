from src.util.graph.Tree import *
#/**
#* A class for producing a tree traversal
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DFSTree:
#/**
#* Whether or not a node has been visited
#*/
 #   boolean[] visited
     def __init__(self):
        self.visited = []
#/**
#* @see graph.GraphTransform#transform(graph.Graph)
#*/
     def transform(self, g):
        self.visited = [False] * g.getNodeCount()
        self.dfs(g.getNode(0))
        result = Tree(g.getNode(0))
        result.setNodes(g.getNodes())
        self.visited = []
        return result
    
    
#/**
#* Perform a depth first search on the graph
#* @param g the graph to search
#*/
     def dfs(self, n):
        self.visited[n.getLabel()] = True
        for i in range(n.getEdgeCount()):
            edge = n.getEdge(i)
            other = edge.getOther(n)
            if (self.visited[other.getLabel()]):
                n.removeEdge(i = i)
                i = i - 1
            else:
                self.dfs(other)
