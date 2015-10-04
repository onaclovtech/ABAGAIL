
#/**
#* A class representing a weighted edge
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class WeightedEdge extends Edge (Comparable):
    
#/**
#* The weight of the edge
#*/
    double weight
    
#/**
#* Make a new weighted edge
#* @param weight the weight of the edge
#*/
     WeightedEdge(double weight):
        self.weight = weight
    }

#/**
#* Get the weight
#* @return the weight
#*/
     double getWeight():
        return weight
    }

#/**
#* Set the weight
#* @param d the new weight
#*/
      setWeight(double d):
        weight = d
    }

#/**
#* @see java.lang.Comparable#compareTo(java.lang.Object)
#*/
     int compareTo(Object o):
        WeightedEdge e = (WeightedEdge) o
        if (getWeight() > e.getWeight()):
            return 1
        } else if (getWeight() < e.getWeight()):
            return -1
        } else {
            return 0
        }
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return super.toString() + " x " + weight
    }

}
