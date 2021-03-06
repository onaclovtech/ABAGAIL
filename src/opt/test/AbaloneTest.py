import csv
from .src.func.nn.backprop.BackPropagationNetworkFactory import *
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
      self.set = DataSet(instances)
      self.networks = BackPropagationNetwork[3]
      self.nnop = NeuralNetworkOptimizationProblem[3]
      self.oa = OptimizationAlgorithm[3]
      self.oaNames = {"RHC", "SA", "GA"}
      self.results = ""
      self.df = DecimalFormat("0.000")

   def run(args):
        for i in range(len(oa)):
            networks[i] = factory.createClassificationNetwork({inputLayer, hiddenLayer, outputLayer})
            nnop[i] = NeuralNetworkOptimizationProblem(set, networks[i], measure)

        oa[0] = RandomizedHillClimbing(nnop[0])
        oa[1] = SimulatedAnnealing(1E11, .95, nnop[1])
        oa[2] = StandardGeneticAlgorithm(200, 100, 10, nnop[2])

        for i in range(len(oa)):
            start = System.nanoTime()
            correct = 0
            incorrect = 0
            train(oa[i], networks[i], oaNames[i]) #trainer.train()
            end = System.nanoTime()
            trainingTime = end - start
            trainingTime /= Math.pow(10,9)

            optimalInstance = oa[i].getOptimal()
            networks[i].setWeights(optimalInstance.getData())
            start = System.nanoTime()
            for j in range(len(instances)):
                networks[i].setInputValues(instances[j].getData())
                networks[i].run()

                predicted = Double.parseDouble(instances[j].getLabel().toString())
                actual = Double.parseDouble(networks[i].getOutputValues().toString())

                # Fix this
                #trash = Math.abs(predicted - actual) < 0.5 ? correct++ : incorrect++

            end = System.nanoTime()
            testingTime = end - start
            testingTime /= Math.pow(10,9)

            #results +=  "\nResults for " + oaNames[i] + ": \nCorrectly classified " + correct + " instances." +
            #            "\nIncorrectly classified " + incorrect + " instances.\nPercent correctly classified: "
            #            + df.format(correct/(correct+incorrect)*100) + "%\nTraining time: " + df.format(trainingTime)
            #            + " seconds\nTesting time: " + df.format(testingTime) + " seconds\n"
        

       # System.out.println(results)
    

   def train(self, oa, network, oaName):
        print ("\nError results for " + oaName + "\n---------------------------")

        for i in range(trainingIterations):
            oa.train()
           
            error = 0
            for j in range(len(instances)):
                network.setInputValues(instances[j].getData())
                network.run()

                output = instances[j].getLabel()
                example = Instance(network.getOutputValues())
                example.setLabel(Instance(Double.parseDouble(network.getOutputValues().toString())))
                error += measure.value(output, example)
            

            System.out.println(df.format(error))
        
    

   def initializeInstances(self):

      #attributes = double[4177][][]
      # Basically read the CSV.
      attributes = []
      with open('abalone.txt', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in spamreader:
            attributes.append(row)
            if row[-1] < 15:
               attributes[-1].append(str(0))
            else:
               attributes[-1].append(str(1))

      return attributes

if __name__ == '__main__':
   blah = AbaloneTest()
   print AbaloneTest