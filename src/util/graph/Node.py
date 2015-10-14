#/**
#* A node in a graph
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Node:
#/**
#* The list of edges
#*/
#    List edges
    
#/**
#* Generic label stored on the node
#*/
 #   int label
    
#/**
#* Make a new node
#*/
    def __init__(self,label = None):
        self.edges = []
        if not label is None:
            self.label = label
#/**
#* Add a edge
#* @param e the edge to add
#*/
    def addEdge(self,e):
        self.edges.append(e)
    
# #/**
# #* Get the edge count
# #* @return the edge count
# #*/
    def getEdgeCount(self):
        return len(self.edges)
    # }
    
# #/**
# #* Remove an edge
# #* @param i the edge to remove
# #*/
#    def removeEdge(self, i, edge):
#        self.edges.remove(i)
#    # }
    
# #/**
# #* Remove an edge
# #* @param edge the edge to remove
# #*/
    def removeEdge(self, i=-1, edge= None):
        if not edge is None:
            self.edges.remove(edge)
        elif i != -1:
            self.edges.pop(i)
            
    # }
    
# #/**
# #* Get an edge
# #* @param i the edge to get
# #* @return the edge
# #*/
    def getEdge(self, i):
        #print "Node.getEdge" + str(self.edges[i])
        return self.edges[i] # cast< (Edge) I suspect I need a [i] instead of get(i) 
    # }
    
    
#/**
#* Connect to another node
#* @param other the other node
#* @param link the link
#*/
    def connect(self, other, link):
        link.setA(self)
        link.setB(other)
        self.edges.append(link)
        other.addEdge(link)
    
    
# #/**
# #* Connect to another node
# #* @param other the other node
# #* @param link the link
# #*/
      # connectDirected(Node other, Edge link):
        # link.setA(self)
        # link.setB(other)
        # edges.add(link)
    # }

# #/**
# #* Get the generic label
# #* @return the label
# #*/
    def getLabel(self):
        return self.label
    # }

#/**
#* Set the label
#* @param label the label
#*/
    def setLabel(self, label):
        self.label = label

# #/**
# #* Get the list of edges
# #* @return the edges
# #*/
    def getEdges(self):
        return self.edges
    # }

# #/**
# #* Set the list of edges
# #* @param list the list of edges
# #*/
    def setEdges(self, list):
        self.edges = list
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
        # return label + " : " + edges
    # }

# }
