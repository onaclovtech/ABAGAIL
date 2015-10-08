import csv
import time
from src.func.nn.backprop.BackPropagationNetworkFactory import *
from src.func.nn.backprop.BackPropagationNetwork import *
from src.opt.example.NeuralNetworkOptimizationProblem import *
from src.opt.OptimizationAlgorithm import *
from src.opt.RandomizedHillClimbing import *
from src.opt.SimulatedAnnealing import *
from src.opt.ga.StandardGeneticAlgorithm import *
from src.shared.SumOfSquaresError import *
from src.shared.DataSet import *


#/**
#* Implementation of randomized hill climbing, simulated annealing, and genetic algorithm to
#* find optimal weights to a neural network that is classifying abalone as having either fewer 
#* or more than 15 rings. 
#*
#* @author Hannah Lau
#* @version 1.0
#*/
class AbaloneTest:
   def __init__(self):
      self.instances = self.initializeInstances()
      self.inputLayer = 7
      self.hiddenLayer = 5
      self.outputLayer = 1
      self.trainingIterations = 1000
      self.factory = BackPropagationNetworkFactory()
      self.measure = SumOfSquaresError()
      self.set = DataSet(self.instances)
      self.networks = [None] * 3
      self.nnop = [None] * 3
      self.oa = [None] * 3
      self.oaNames = ["RHC", "SA", "GA"]
      self.results = ""

   def run(self):
        for i in range(len(self.oa)):
            self.networks[i] = self.factory.createClassificationNetwork([self.inputLayer, self.hiddenLayer, self.outputLayer])
            self.nnop[i] = NeuralNetworkOptimizationProblem(self.set, self.networks[i], self.measure)
        print "abalone.test.self.networks[0]" + str(self.networks[0])
        self.oa[0] = RandomizedHillClimbing(self.nnop[0])
        self.oa[1] = SimulatedAnnealing(1E11, .95, self.nnop[1])
        self.oa[2] = StandardGeneticAlgorithm(200, 100, 10, self.nnop[2])

        for i in range(len(self.oa)):
            start = time.time()
            correct = 0
            incorrect = 0
            self.train(self.oa[i], self.networks[i], self.oaNames[i]) #trainer.train()
            end = System.nanoTime()
            trainingTime = end - start

            optimalInstance = self.oa[i].getOptimal()
            self.networks[i].setWeights(optimalInstance.getData())
            start = System.nanoTime()
            for j in range(len(self.instances)):
                self.networks[i].setInputValues(self.instances[j].getData())
                self.networks[i].run()

                predicted = Double.parseDouble(self.instances[j].getLabel().toString())
                actual = Double.parseDouble(self.networks[i].getOutputValues().toString())

                # Fix this, although it never is used, which is odd
                #trash = Math.abs(predicted - actual) < 0.5 ? correct++ : incorrect++

            end = time.time()
            testingTime = end - start

             
            results =  ["\nResults for " + self.oaNames[i] + ": \nCorrectly classified " + correct + " instances.",
                       "\nIncorrectly classified " + incorrect + " instances.\nPercent correctly classified: ",
                       float(correct)/(correct+incorrect)*100 + "%\nTraining time: " + trainingTime,
                       " seconds\nTesting time: " + testingTime + " seconds\n"]
        
            print results
       # System.out.println(results)
    

   def train(self, oa, network, oaName):
        print ("\nError results for " + oaName + "\n---------------------------")

        for i in range(self.trainingIterations):
            oa.train()

            error = 0
            for j in range(len(self.instances)):
                network.setInputValues(self.instances[j].getData())
                network.run()

                output = self.instances[j].getLabel()
                print "abalonetest.train.network.getOutputValues(): " + str(network.getOutputValues().__class__)
                example = Instance(data = network.getOutputValues())
                example.setLabel(Instance(val = network.getOutputValues()))
                error += self.measure.value(output, example)
            

            System.out.println(df.format(error))
        
    

   def initializeInstances(self):

      #attributes = double[4177][][]
      # Basically read the CSV.
      attributes = []
      with open('./src/opt/test/abalone.txt', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in spamreader:
            if row[-1] < 15:
               attributes.append([row[:-1], row[-1], 0])
            else:
               attributes.append([row[:-1], row[-1], 1])
                
      instances = [len(attributes)]

      for i in range(len(instances)):
         instances[i] = Instance(ds = attributes[i][0])
         instances[i].setLabel(Instance(val = attributes[i][2]))
      return instances


if __name__ == '__main__':
   blah = AbaloneTest()
   print blah.run()