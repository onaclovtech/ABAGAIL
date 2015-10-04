

#/**
#* A node in a graph
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Node {
#/**
#* The list of edges
#*/
    List edges
    
#/**
#* Generic label stored on the node
#*/
    int label
    
#/**
#* Make a new node
#*/
     Node():
        edges = new ArrayList()
    }
    
#/**
#* Make a new node
#* @param data the data
#*/
     Node(int label):
        self()
        self.label = label
    }
    
#/**
#* Add a edge
#* @param e the edge to add
#*/
      addEdge(Edge e):
        edges.add(e)
    }
    
#/**
#* Get the edge count
#* @return the edge count
#*/
     int getEdgeCount():
        return edges.size()
    }
    
#/**
#* Remove an edge
#* @param i the edge to remove
#*/
      removeEdge(int i):
        edges.remove(i)
    }
    
#/**
#* Remove an edge
#* @param edge the edge to remove
#*/
      removeEdge(Edge edge):
        edges.remove(edge)
    }
    
#/**
#* Get an edge
#* @param i the edge to get
#* @return the edge
#*/
     Edge getEdge(int i):
        return (Edge) edges.get(i)
    }
    
    
#/**
#* Connect to another node
#* @param other the other node
#* @param link the link
#*/
      connect(Node other, Edge link):
        link.setA(self)
        link.setB(other)
        edges.add(link)
        other.addEdge(link)
    }
    
#/**
#* Connect to another node
#* @param other the other node
#* @param link the link
#*/
      connectDirected(Node other, Edge link):
        link.setA(self)
        link.setB(other)
        edges.add(link)
    }

#/**
#* Get the generic label
#* @return the label
#*/
     int getLabel():
        return label
    }

#/**
#* Set the label
#* @param label the label
#*/
      setLabel(int label):
        self.label = label
    }

#/**
#* Get the list of edges
#* @return the edges
#*/
     List getEdges():
        return edges
    }

#/**
#* Set the list of edges
#* @param list the list of edges
#*/
      setEdges(List list):
        edges = list
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return label + " : " + edges
    }

}
