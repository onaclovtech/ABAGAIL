from src.util.graph.Edge import *

#/**
#* A class representing a weighted edge
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class WeightedEdge (Edge):# (Comparable):
    
#/**
#* The weight of the edge
#*/
#    double weight
    
#/**
#* Make a new weighted edge
#* @param weight the weight of the edge
#*/
    def __init__(self, weight):
        Edge.__init__(self)
        self.weight = weight

#/**
#* Get the weight
#* @return the weight
#*/
    def getWeight(self):
        return self.weight
    # }

# #/**
# #* Set the weight
# #* @param d the new weight
# #*/
    def setWeight(self, d):
        self.weight = d
    # }

# #/**
# #* @see java.lang.Comparable#compareTo(java.lang.Object)
# #*/
     # int compareTo(Object o):
        # WeightedEdge e = (WeightedEdge) o
        # if (getWeight() > e.getWeight()):
            # return 1
        # } else if (getWeight() < e.getWeight()):
            # return -1
        # } else {
            # return 0
        # }
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
        # return super.toString() + " x " + weight
    # }

# }
