

#/**
#* A class repsenting a graph
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Graph:
#/**
#* The list of nodes
#*/
    #List nodes
    
#/**
#* Make a new graph
#*/
     def __init__(self):
        self.nodes = []

    
#/**
#* Add a node
#* @param n the node to add
#*/
     def addNode(self, n):
        n.setLabel(self.getNodeCount())
        self.nodes.append(n)
    
#/**
#* Get a node
#* @param i the node to get
#* @return the node
#*/
     def getNode(self, i):
        return self.nodes[i]
    
    
#/**
#* Get the number of nodes in the graph
#* @return the number of nodes
#*/
     def getNodeCount(self):
        return len(self.nodes)
    
# #/**
# #* Get the set of edges
# #* @return the edges
# #*/
     def getEdges(self):
        result = []
        for i in range(self.getNodeCount()):
            result = result + self.getNode(i).getEdges()
        # }
        return result
    # }
# #/**
# #* Get the nodes
# #* @return the nodes
# #*/
     def getNodes(self):
        return self.nodes
    # }

# #/**
# #* Set the nodes
# #* @param list the nodes
# #*/
     def setNodes(self, list):
        self.nodes = list
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     def toString(self):
       result = []
       for i in range(self.getNodeCount()):
           print "graph.getNode()" + str(self.getNode(i).getLabel())
           result.append(str(self.getNode(i).getLabel())) 
       # }
       return '\n'.join(result)
    # }

# }
