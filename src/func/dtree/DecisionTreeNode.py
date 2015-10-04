
#/**
#* A node in a decision tree
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DecisionTreeNode {
    
#/**
#* The split used on self node for a non leaf node, or null for a leaf
#*/
    DecisionTreeSplit split
    
#/**
#* The statistics for the split for a non leaf node, or null for a leaf
#*/
    DecisionTreeSplitStatistics stats

#/**
#* The child nodes for a non leaf node, or null for a leaf
#*/
    DecisionTreeNode[] nodes
    
#/**
#* Create a new non leaf node
#* @param split the split
#* @param stast the stats
#* @param nodes the children nodes
#*/
     DecisionTreeNode(DecisionTreeSplit split,
            DecisionTreeSplitStatistics stats, DecisionTreeNode[] nodes):
        self.split = split
        self.stats = stats
        self.nodes = nodes
    }
    
#/**
#* Whether all of self node's children are null
#* @return true if they are
#*/
     boolean isLeaf():
        for (int i = 0 i < nodes.length i++):
            if (nodes[i] != null):
                return false
            }
        }
        return true
    }

#/**
#* Get the split for a non leaf node
#* @return the split
#*/
     DecisionTreeSplit getSplit():
        return split
    }

#/**
#* Get the splist statistics for a non leaf node
#* @return the split statistics
#*/
     DecisionTreeSplitStatistics getSplitStatistics():
        return stats
    }

#/**
#* Get the child nodes for the decision tree
#* @return the child nodes
#*/
     DecisionTreeNode[] getNodes():
        return nodes
    }

#/**
#* Get a node
#* @param branch the branch to get the node for
#*/
     DecisionTreeNode getNode(int branch):
        return nodes[branch]
    }
    
#/**
#* Get a string representation
#* @param indentation the level of indentation
#* @return the string representation
#*/
     String toString(String indentation):
        String ret = indentation + split.toString() + "\n"
        for (int i = 0 i < nodes.length i++):
            if (nodes[i] != null):
                ret += nodes[i].toString("\t" + indentation)
            } else {
                double[] probabilities
                if (stats.getInstanceCount(i) == 0):
                    probabilities = stats.getClassProbabilities()
                } else {
                    probabilities = stats.getConditionalClassProbabilities(i)
                }
                ret += indentation
                for (int j = 0 j < probabilities.length j++):
                    ret += probabilities[j] + " "
                }
                ret += "\n"
            }
        }
        return ret
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return toString("")
    }

}
