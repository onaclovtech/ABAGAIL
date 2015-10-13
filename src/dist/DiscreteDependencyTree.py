from src.dist.AbstractDistribution import *
from src.shared.DataSetDescription import *
from src.util.linalg.DenseVector import *
from src.shared.DataSet import *
from src.dist.DiscreteDependencyTreeRootNode import *
import math
#/**
#* A discrete dependency distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DiscreteDependencyTree(AbstractDistribution):
#/**
#* The dependency tree root
#*/
    #DiscreteDependencyTreeRootNode root
    
#/**
#* The tree
#*/
    #Tree dt
    
#/**
#* The m value
#*/
   # double m
    
#/**
#* Description the data set
#*/
    #DataSetDescription description
    
#/**
#* Make a discrete dependency tree distribution
#* @param m the small positive value to add when making the tree
#*/
     def __init__(self, m = None, ranges = None):
        if not m is None:
            if not isinstance(m, (int, long, float, complex)):
               raise TypeError("Expecting number got" + str(m.__class__))
            self.m = m
        if not ranges is None:
            if not isinstance(ranges, list):
               raise TypeError("Expecting list got" + str(m.__class__))
            self.description = DataSetDescription()
            self.description.setMinVector(DenseVector(size = len(ranges)))
            max = DenseVector(size = len(ranges))
            for i in range(max.size()):
               max.set(i, ranges[i] - 1)
            self.description.setMaxVector(max)
            
        # Initialize other variables for use
        self.dt = None
        self.root = None

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     def p(i):
        if not isinstance(i,Instance):
            raise TypeError("Expected Instance got" + str(i.__class__))
        return self.root.probabilityOf(i)

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     def sample(self):
        if not isinstance(ignored,Instance):
            raise TypeError("Expected Instance got" + str(ignored.__class__))
        i = Instance(data = DenseVector(size = self.dt.getNodeCount()))
        self.root.generateRandom(i)
        return i
    

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     def mode(self,ignored):
        if not isinstance(ignored,Instance):
            raise TypeError("Expected Instance got" + str(ignored.__class__))
        i = Instance(data = DenseVector(size = self.dt.getNodeCount()))
        self.root.generateMostLikely(i)
        return i
    

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
     def estimate(self, observations):
        if not isinstance(observations,DataSet):
            raise TypeError("Expected Instance got" + str(observations.__class__))
        if (not self.description is None):
            observations.setDescription(self.description)
        else:
            if (observations.getDescription() == null):
                observations.setDescription(DataSetDescription(observations))
        mutualI = self.calculateMutualInformation(observations)
        # construct the graph
        rg = buildDirectedMST(observations, mutualI)
        # make the dependency tree
        self.dt = Tree()
        self.root = DiscreteDependencyTreeRootNode(observations, rg.getRoot(), self.m, self.dt)
        self.dt.setRoot(self.root)
        
    

#/**
#* Build the directed mst from the mutual information
#* and ranges
#* @param ranges the ranges
#* @param mutualI the mutual information values
#* @return the directed mst
#*/
     def buildDirectedMST(self, observations, mutualI):
        if not isinstance(observations,DataSet):
            raise TypeError("Expected Instance got" + str(observations.__class__))
        if not isinstance(mutualI,list):
            raise TypeError("Expected Instance got" + str(mutualI.__class__))
        g = Graph()
        for i in range(observations.get(0).size()):
            n = Node(i)
            g.addNode(n)
        for i in range(observations.get(0).size()):
            for j in range(i):
                a = g.getNode(i)
                b = g.getNode(j)
                a.connect(b, WeightedEdge(-mutualI[i][j]))
        # find the mst
        g = KruskalsMST().transform(g)
        # direct it
        rg = DFSTree().transform(g)
        return rg
    

#/**
#* Calculate the mutual information from the data
#* @param ranges the ranges of the data
#* @param data the data itself
#* @return the mutual informations
#*/
     def calculateMutualInformation(self, observations):
        if not isinstance(observations,DataSet):
            raise TypeError("Expected Instance got" + str(observations.__class__))
        dsd = observations.getDescription()
        # probs[i][j] is the probability that x_i = j
        probs = [None] * observations.get(0).size()
        for i in range(len(probs)):
            probs[i] = [None] * dsd.getDiscreteRange(i)
        weightSum = 0.0
        # fill in probs
        for i in range(observations.size()):
            for  j in range(observations.get(i).size()):
                probs[j][observations.get(i).getDiscrete(j)] = probs[j][observations.get(i).getDiscrete(j)] + observations.get(i).getWeight()
            weightSum = weightSum + observations.get(i).getWeight()
        # normalize
        for i in range(len(probs)):
            for j in range(len(probs[i])):
                probs[i][j] /= weightSum
        # calculate the entropies of the different variables
        entropies = [None] * observations.get(0).size()
        for i in range(observations.get(0).size()):
            for j in range(dsd.getDiscreteRange(i)):
                if (probs[i][j] != 0):
                    entropies[i] -= probs[i][j] * math.log(probs[i][j])
        # calculate the mutual information between all variables
        mutualI = [None] * observations.get(0).size()
        for i in range(len(mutualI)):
            mutualI[i] = [None] * i
            for j in range(i):
                # the joint probabilities
                # joints[a][b] is the probability that x_i = a && x_j = b
                joints = [None] * dsd.getDiscreteRange(i)
                for i in range(len(joints)):
                    joints[i] = [None] * dsd.getDiscreteRange(j)
                # fill in the joints
                for k in range(observations.size()):
                    instance = observations.get(k)
                    joints[instance.getDiscrete(i)][instance.getDiscrete(j)] = joints[instance.getDiscrete(i)][instance.getDiscrete(j)] + 1
                # normalize
                for k in range(len(joints)):
                    for l in range(len(joints[k])):
                        joints[k][l] /= weightSum
                # calculate the mutual information I(x_i x_j)
                # add the entropy of x_i
                mutualI[i][j] += entropies[i]
                # and the entropy of x_j
                mutualI[i][j] += entropies[j]
                # subtract the joint entropy
                for k in range(len(joints)):
                    for l in range(len(joints[k])):
                        if (joints[k][l] != 0):
                            mutualI[i][j] += joints[k][l] * math.log(joints[k][l])

        return mutualI


#/**
#* @see java.lang.Object#toString()
#*/
     def toString(self):
        return self.dt.toString()
