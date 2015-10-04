
#/**
#* An edge
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Edge {
#/**
#* The in node
#*/
    Node a
#/**
#* The out node
#*/
    Node b

#/**
#* Get the in node
#* @return the in node
#*/
     Node getA():
        return a
    }

#/**
#* Get the out node
#* @return the out node
#*/
     Node getB():
        return b
    }
    
#/**
#* Get the other node
#* @param n the node
#* @return the other node
#*/
     Node getOther(Node n):
        if (n == a):
            return b
        } else {
            return a
        }
    }

#/**
#* Set the in node
#* @param node the in node
#*/
      setA(Node node):
        a = node
    }

#/**
#* Set the out node
#* @param node the out node
#*/
      setB(Node node):
        b = node
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
       return a.getLabel() + " -> " + b.getLabel() 
    }

}
