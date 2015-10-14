from src.util.graph.Node import *
from src.dist.DiscreteDependencyTreeNode import *

#/**
#* A root node in a discrete dependency tree
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DiscreteDependencyTreeRootNode(Node):
#/**
#* The unconditional probabilities
#*/
#    double[] probabilities
    
#/**
#* Build a dependency tree root out of the given node
#* @param node the node to build the root out of
#* @param ranges the ranges of the values
#* @param data the data itself
#*/
     def __init__(self, dataSet, node, m, t):
     #DataSet dataSet, Node node, double m,  Tree t
        dsd = dataSet.getDescription()
        self.probabilities = [0.0] * dsd.getDiscreteRange(node.getLabel())
        weightSum = 0.0
        for i in range(dataSet.size()):
            self.probabilities[dataSet.get(i).getDiscrete(node.getLabel())] += dataSet.get(i).getWeight()
            weightSum += dataSet.get(i).getWeight()
        
        for i in range(len(self.probabilities)):
            self.probabilities[i] = (self.probabilities[i] + m / len(self.probabilities)) / (weightSum + m)
        t.addNode(self)
        self.setLabel(node.getLabel())
        for i in range(node.getEdgeCount()):
            dtn = DiscreteDependencyTreeNode(dataSet, node.getEdge(i).getOther(node), node.getLabel(), m, t)
            connectDirected(dtn, Edge())
        
    
# #/**
# #* Calculate the probability
# #* @param instance the instance
# #* @return the probability
# #*/
     # double probabilityOf(Instance instance):
        # DiscreteDistribution dd = new DiscreteDistribution(probabilities)
        # double p = dd.p(new Instance(instance.getDiscrete(getLabel())))
        # for (int i = 0 i < getEdgeCount() i++):
            # DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            # p *= dtn.probabilityOf(instance)
        # }
        # return p
    # }
    
# #/**
# #* Sample from the root of the tree
# #* @param node the root of the tree
# #*/
      # generateRandom(Instance instance):
        # DiscreteDistribution dd = new DiscreteDistribution(probabilities)
        # instance.getData().set(getLabel(), dd.sample(null).getDiscrete())
        # for (int i = 0 i < getEdgeCount() i++):
            # DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            # dtn.generateRandom(instance)
        # }
    # }
    
# #/**
# #* Sample from the root of the tree
# #* @param node the root of the tree
# #*/
      # generateMostLikely(Instance instance):
        # DiscreteDistribution dd = new DiscreteDistribution(probabilities)
        # instance.getData().set(getLabel(), dd.mode(null).getDiscrete())
        # for (int i = 0 i < getEdgeCount() i++):
            # DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            # dtn.generateMostLikely(instance)
        # }
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
       # return super.toString() + "\n" + ABAGAILArrays.toString(probabilities) 
    # }

# }
