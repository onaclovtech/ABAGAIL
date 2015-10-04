



#/**
#* A class for performing neural network optimzation
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class NeuralNetworkOptimizationProblem (HillClimbingProblem), GeneticAlgorithmProblem {

#/**
#* The evaluation function
#*/
    EvaluationFunction eval
#/**
#* The cross over function
#*/
    CrossoverFunction crossover
#/**
#* The neighbor function
#*/
    NeighborFunction neighbor
#/**
#* The mutation function
#*/
    MutationFunction mutate
#/**
#* The distribution
#*/
    Distribution dist
    
#/**
#* Make a new neural network optimization
#* @param examples the examples
#* @param network the neural network
#* @param measure the error measure
#*/
     NeuralNetworkOptimizationProblem(DataSet examples,
             NeuralNetwork network, ErrorMeasure measure):
        eval = new NeuralNetworkEvaluationFunction(network, examples, measure)
        crossover = new UniformCrossOver()
        neighbor = new ContinuousAddOneNeighbor()
        mutate = new ContinuousAddOneMutation()
        dist = new NeuralNetworkWeightDistribution(network.getLinks().size())
    }

#/**
#* @see opt.OptimizationProblem#value(opt.OptimizationData)
#*/
     double value(Instance d):
        return eval.value(d)
    }

#/**
#* @see opt.OptimizationProblem#random()
#*/
     Instance random():
        return dist.sample(null)
    }

#/**
#* @see opt.OptimizationProblem#neighbor(opt.Instance)
#*/
     Instance neighbor(Instance d):
        return neighbor.neighbor(d)
    }
    

#/**
#* @see opt.GeneticAlgorithmProblem#mate(opt.Instance, opt.Instance)
#*/
     Instance mate(Instance da, Instance db):
        return crossover.mate(da, db)
    }

#/**
#* @see opt.GeneticAlgorithmProblem#mutate(opt.Instance)
#*/
      mutate(Instance d):
        mutate.mutate(d)
    }

}
