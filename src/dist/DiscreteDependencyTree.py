from src.dist.AbstractDistribution import *
from src.shared.DataSetDescription import *
from src.util.linalg.DenseVector import *
from src.shared.DataSet import *
from src.dist.DiscreteDependencyTreeRootNode import *
from src.util.graph.Graph import *
from src.util.graph.WeightedEdge import *
from src.util.graph.KruskalsMST import *
from src.util.graph.DFSTree import *

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
        rg = self.buildDirectedMST(observations, mutualI)
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
#        print "DiscreteDependencyTree.buildDirectedMST.g" + str(g.__class__)
#        print "DiscreteDependencyTree.buildDirectedMST.g" + str(g.toString())
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
        #print "Discrete.Dependency.Tree.calculateMutualInformation.observatinos.size" + str(observations.get(0).size())
        dsd = observations.getDescription()
        # probs[i][j] is the probability that x_i = j
        probs = [0.0] * observations.get(0).size()
        for i in range(len(probs)):
            probs[i] = [0.0] * dsd.getDiscreteRange(i)
        weightSum = 0.0
        # fill in probs
        #print "probs.size" + str(len(probs))
        #print "probs[0].size" + str(len(probs[0]))
        for i in range(observations.size()):
            for  j in range(observations.get(i).size()):
                #print "DiscreteDependencyTree.calc.observations.get(i).getDiscrete(j).i:" + str(i) + "j:" + str(j) + "final: " + str(observations.get(i).getDiscrete(j))
                #print "DiscreteDependencyTree.calc.observations.get(i).getDiscrete(j).i:" + str(i) + "j:" + str(j) + "final: " + str(observations.get(i).getDiscrete(j))
                probs[j][observations.get(i).getDiscrete(j)] = probs[j][observations.get(i).getDiscrete(j)] + observations.get(i).getWeight()
            weightSum = weightSum + observations.get(i).getWeight()
        # normalize
        for i in range(len(probs)):
            for j in range(len(probs[i])):
                probs[i][j] /= weightSum
        # calculate the entropies of the different variables
        entropies = [0.0] * observations.get(0).size()
        for i in range(observations.get(0).size()):
            for j in range(dsd.getDiscreteRange(i)):
                if (probs[i][j] != 0):
                    entropies[i] -= probs[i][j] * math.log(probs[i][j])
        # calculate the mutual information between all variables
        mutualI = [0.0] * observations.get(0).size()
        i = 0
        for i in range(len(mutualI)):
            mutualI[i] = [0.0] * i
            # Small concerns here. I think it's a little surprising that the last element mutualI[59][59] never gets set. I'm not sure if that's an expected scenario, love to compare to java
            for j in range(i):
                # the joint probabilities
                # joints[a][b] is the probability that x_i = a && x_j = b
                joints = [0.0] * dsd.getDiscreteRange(i)
                for p in range(len(joints)):
                    joints[p] = [0.0] * dsd.getDiscreteRange(j)
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
                
                # I believe this is a workaround for java, basically in the case of a 0 size array it's null, I'm *assuming* that it's simply throwing away the operation.
                if len(mutualI[i]) > 0:
                    #print "DDT.mutual.lens,entropieslens" + str(len(mutualI)) + " mutual[i] len " + str(len(mutualI[i])) + "entropie len" + str(len(entropies)) + "i" + str(i) + "j" + str(j)
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
