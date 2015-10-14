


#/**
#* A node in a discrete dependency tree
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
DiscreteDependencyTreeNode (Node):
#/** 
#* The conditional probabilities 
#*/
   # double[][] probabilities
#/**
#* The parent
#*/
    #int parent
    
#/**
#* Make a dependency tree node
#* @param ranges the ranges of the data
#* @param data the data itself
#* @param node the node
#* @param parent the parent node index
#* @param m the bayesian estimate parameter
#* @param t the tree
#*/
    def __init__(self, DataSet dataSet, Node node, int parent, double m, Tree t):
        # DataSet dataSet, Node node, int parent, double m, Tree t
        dsd = dataSet.getDescription()
        probabilities = [0.0] * dsd.getDiscreteRange(parent)
        for i in range(len(probabilities)):
            probabilities[i] = [0.0] * dsd.getDiscreteRange(node.getLabel())
        sums = [0.0] * dsd.getDiscreteRange(parent)
        for i in range(len(dataSet)):
            probabilities[dataSet.get(i).getDiscrete(parent)][dataSet.get(i).getDiscrete(node.getLabel())] += dataSet.get(i).getWeight()
            sums[dataSet.get(i).getDiscrete(parent)] += dataSet.get(i).getWeight()
        for i in range(len(probabilities)):
            for j in range(len(probabilities[i])):
                probabilities[i][j] = (probabilities[i][j] + m / len(probabilities[i])) / (sums[i] + m)
          
        self.probabilities = probabilities
        self.parent = parent
        t.addNode(self)
        self.setLabel(node.getLabel())
        for (int i = 0 i < node.getEdgeCount() i++):
            dtc = new DiscreteDependencyTreeNode(dataSet, node.getEdge(i).getOther(node), node.getLabel(), m, t)
            connectDirected(dtc, new Edge())
    
#/**
#* Calculate the probability
#* @param instance the instance
#* @return the probability
#*/
     double probabilityOf(Instance sample):
        DiscreteDistribution dd = new DiscreteDistribution(
            probabilities[sample.getDiscrete(parent)])
        double p = dd.p(new Instance(sample.getDiscrete(getLabel())))
        for (int i = 0 i < getEdgeCount() i++):
            DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            p *= dtn.probabilityOf(sample)
        }
        return p
    }  

#/**
#* Sample from the node
#* @param sample the sample so far
#*/
      generateRandom(Instance sample):
        DiscreteDistribution dd = new DiscreteDistribution(
            probabilities[sample.getDiscrete(parent)])
        sample.getData().set(getLabel(), dd.sample(null).getDiscrete())
        for (int i = 0 i < getEdgeCount() i++):
            DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            dtn.generateRandom(sample)
        }
    }  
    
#/**
#* Sample from the node
#* @param sample the sample so far
#*/
      generateMostLikely(Instance sample):
        DiscreteDistribution dd = new DiscreteDistribution(
            probabilities[sample.getDiscrete(parent)])
        sample.getData().set(getLabel(), dd.mode(null).getDiscrete())
        for (int i = 0 i < getEdgeCount() i++):
            DiscreteDependencyTreeNode dtn = (DiscreteDependencyTreeNode) getEdge(i).getOther(self)
            dtn.generateRandom(sample)
        }
    }    
      
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return super.toString() + " Parent = " + parent + "\n" + ABAGAILArrays.toString(probabilities)
    }


}
