from src.opt.example.NeuralNetworkEvaluationFunction import *
from src.opt.ga.UniformCrossOver import *
from src.opt.ga.ContinuousAddOneMutation import *
from src.opt.ContinuousAddOneNeighbor import *
from src.opt.example.NeuralNetworkWeightDistribution import *

#/**
#* A class for performing neural network optimzation
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class NeuralNetworkOptimizationProblem:
#/**
#* Make a neural network optimization
#* @param examples the examples
#* @param network the neural network
#* @param measure the error measure
#*/
     def __init__(self, examples, network, measure):
        self.eval = NeuralNetworkEvaluationFunction(network, examples, measure)
        self.crossover = UniformCrossOver()
        self.neighbor = ContinuousAddOneNeighbor()
        self.mutate = ContinuousAddOneMutation()
        self.dist = NeuralNetworkWeightDistribution(network.getLinks().size())
    

#/**
#* @see opt.OptimizationProblem#value(opt.OptimizationData)
#*/
     def value(self, d):
        return eval.value(d)


#/**
#* @see opt.OptimizationProblem#random()
#*/
     def random(self):
        return dist.sample(null)
    

#/**
#* @see opt.OptimizationProblem#neighbor(opt.Instance)
#*/
     def neighbor(self, d):
        return neighbor.neighbor(d)
    
    

#/**
#* @see opt.GeneticAlgorithmProblem#mate(opt.Instance, opt.Instance)
#*/
     def mate(self, da, db):
        return crossover.mate(da, db)
    

#/**
#* @see opt.GeneticAlgorithmProblem#mutate(opt.Instance)
#*/
     def mutate(self, d):
        mutate.mutate(d)
    