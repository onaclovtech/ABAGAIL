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

        self.oa[0] = RandomizedHillClimbing(self.nnop[0])
        self.oa[1] = SimulatedAnnealing(1E11, .95, self.nnop[1])
        self.oa[2] = StandardGeneticAlgorithm(200, 100, 10, self.nnop[2])

        for i in range(len(self.oa)):
            start = time.time()
            correct = 0
            incorrect = 0
            self.train(self.oa[i], self.networks[i], self.oaNames[i]) #trainer.train()
            end = time.time()
            trainingTime = end - start

            optimalInstance = self.oa[i].getOptimal()
            self.networks[i].setWeights(optimalInstance.getData())
            start = time.time()
            for j in range(len(self.instances)):
                self.networks[i].setInputValues(self.instances[j].getData())
                self.networks[i].run()
                predicted = self.instances[j].getLabel().toString()
                actual = self.networks[i].getOutputValues().toString()

                if abs(float(predicted) - float(actual)) < 0.5: 
                    correct = correct + 1
                else:
                    incorrect = incorrect + 1

            end = time.time()
            testingTime = end - start

             
            results =  ["Results for " + self.oaNames[i] + ": ",
                        "Correctly classified " + str(correct) + " instances.",
                        "Incorrectly classified " + str(incorrect) + " instances.",
                        "Percent correctly classified: ",
                       str(float(correct)/(correct+incorrect)*100) + "%",
                       "Training time: " + str(trainingTime) + " seconds",
                       "Testing time: " + str(testingTime) + " seconds"]
        
            print '\n'.join(results)
       # System.out.println(results)
    

   def train(self, oa, network, oaName):
        print ("\nError results for " + oaName + "\n---------------------------")
        res = []
        for i in range(self.trainingIterations):
            oa.train()
            error = 0
            for j in range(len(self.instances)):
                #print "self.instances[j].getData()" + str(self.instances[j].getData())
                network.setInputValues(self.instances[j].getData())
                #print network.__class__
                network.run()

                output = self.instances[j].getLabel()
                #print "abalonetest.train.self.instances[j].getLabel(): " + str(self.instances[j].getLabel().toString())
                print "abalonetest.train.network.getOutputValues(): " + str(network.getOutputValues().toString())
                example = Instance(data = network.getOutputValues())
                example.setLabel(Instance(data = network.getOutputValues()))
                error = error + self.measure.value(output, example)
            

            res.append(error)
        #for a,b,c in zip(res[::3],res[1::3],res[2::3]):
        #    print '{:<10}{:<10}{:<}'.format(a,b,c)
        print res

# 0.455,0.365,0.095,0.514,0.2245,0.101,0.15,15
# 0.35,0.265,0.09,0.2255,0.0995,0.0485,0.07,7
# 0.53,0.42,0.135,0.677,0.2565,0.1415,0.21,9
# 0.44,0.365,0.125,0.516,0.2155,0.114,0.155,10
# 0.33,0.255,0.08,0.205,0.0895,0.0395,0.055,7
# 0.425,0.3,0.095,0.3515,0.141,0.0775,0.12,8
# 0.53,0.415,0.15,0.7775,0.237,0.1415,0.33,20
# 0.545,0.425,0.125,0.768,0.294,0.1495,0.26,16
# 0.475,0.37,0.125,0.5095,0.2165,0.1125,0.165,9
# 0.55,0.44,0.15,0.8945,0.3145,0.151,0.32,19
   def initializeInstances(self):

      #attributes = double[4177][][]
      # Basically read the CSV.
      attributes = []
      with open('./src/opt/test/abalone.txt', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in spamreader:

            if int(row[-1]) < 15:
               attributes.append(row[:-1] + [row[-1]] + [0])
            else:
               attributes.append(row[:-1] + [row[-1]] + [1])
            
      instances = [None] * 100#len(attributes)

      for i in range(len(instances)):
         instances[i] = Instance(ds = attributes[i][:-2])
         #print instances[i].toString()
         instances[i].setLabel(Instance(val = attributes[i][-1]))
         #print attributes[i][-1]
         #print "instances[i].getLabel().toString()" + str(instances[i].getLabel().toString())
         
      return instances


if __name__ == '__main__':
   blah = AbaloneTest()
   print blah.run()