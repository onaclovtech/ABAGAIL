
#/**
#* An edge
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Edge:
#/**
#* The in node
#*/
    # Node a
# #/**
# #* The out node
# #*/
    # Node b
    def __init__(self):
        self.a = None
        self.b = None
#/**
#* Get the in node
#* @return the in node
#*/
    def getA(self):
        return self.a
    

# #/**
# #* Get the out node
# #* @return the out node
# #*/
    def getB(self):
        return self.b
    
# #/**
# #* Get the other node
# #* @param n the node
# #* @return the other node
# #*/
    def getOther(self,n):
        if (n == self.a):
            return self.b
        else:
            return self.a
        
# #/**
# #* Set the in node
# #* @param node the in node
# #*/
    def setA(self,node):
        self.a = node
        #print "Edge:" + str(self.a.__class__)
    # }

# #/**
# #* Set the out node
# #* @param node the out node
# #*/
    def setB(self,node):
        self.b = node
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
       # return a.getLabel() + " -> " + b.getLabel() 
    # }

# }
