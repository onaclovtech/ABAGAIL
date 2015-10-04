

#/**
#* A class repsenting a graph
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Graph {
#/**
#* The list of nodes
#*/
    List nodes
    
#/**
#* Make a new graph
#*/
     Graph():
        nodes = new ArrayList()
    }
    
#/**
#* Add a node
#* @param n the node to add
#*/
      addNode(Node n):
        n.setLabel(getNodeCount())
        nodes.add(n)
    }
    
#/**
#* Get a node
#* @param i the node to get
#* @return the node
#*/
     Node getNode(int i):
        return (Node) nodes.get(i)
    }
    
#/**
#* Get the number of nodes in the graph
#* @return the number of nodes
#*/
     int getNodeCount():
        return nodes.size()
    }
    
#/**
#* Get the set of edges
#* @return the edges
#*/
     Set getEdges():
        Set set = new HashSet()
        for (int i = 0 i < getNodeCount() i++):
            set.addAll(getNode(i).getEdges())
        }
        return set
    }
#/**
#* Get the nodes
#* @return the nodes
#*/
     List getNodes():
        return nodes
    }

#/**
#* Set the nodes
#* @param list the nodes
#*/
      setNodes(List list):
        nodes = list
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
       String result = ""
       for (int i = 0 i < getNodeCount() i++):
           result += getNode(i) + "\n" 
       }
       return result
    }

}
