

#/**
#* A node in a KDTree
#*/
 class KDTreeNode (Serializable), Comparable {
#/**
#* The key corresponding to self node
#*/
    Instance instance
    
#/**
#* The dimension along which self node is split
#*/
    int dimension
    
#/**
#* The tree that is smaller along the chosen dimension
#*/
    KDTreeNode left
    
#/**
#* The tree that is bigger along the chosen dimension
#*/
    KDTreeNode right
    
#/**
#* Create a new KDTreeNode
#* @param key the key for the node
#* @param data the the data
#*/
     KDTreeNode(Instance key):
        self.instance = key
    }
    
#/**
#* Get the value of self node in the split dimension
#* @return the value
#*/
     double getSplitValue():
        return instance.getContinuous(dimension)
    }
    
#/**
#* Get the key for self node
#* @return the key 
#*/
     Instance getInstance():
        return instance
    }
    
#/**
#* Set the dimension
#* @param dimension the dimension
#*/
      setDimension(int dimension):
        self.dimension = dimension
    }
    
#/**
#* Get the dimension along which self node is split
#* @return the dimension
#*/
     int getDimension():
        return dimension
    }
    
#/**
#* Get the left node
#* @return the left node
#*/
     KDTreeNode getLeft():
        return left
    }
    
#/**
#* Set the left node
#* @param node the left node
#*/
      setLeft(KDTreeNode node):
        left = node
    }
    
#/**
#* Get the right node
#* @return the right node
#*/
     KDTreeNode getRight():
        return right
    }
    
#/**
#* Set the right node 
#* @param node the node
#*/
      setRight(KDTreeNode node):
        right = node
    }

#/**
#* @see java.lang.Comparable#compareTo(java.lang.Object)
#*/
     int compareTo(Object o):
        double value = getSplitValue()
        double otherValue = ((KDTreeNode) o).getInstance().getContinuous(dimension)
        if (value < otherValue):
            return -1
        } else if (value > otherValue):
            return 1
        } else {
            return 0
        }
    }
}
