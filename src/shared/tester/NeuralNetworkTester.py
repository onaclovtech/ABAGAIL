

#/**
#* A tester for neural networks.  This will run each instance
#* through the network and report the results to any test metrics
#* specified at instantiation.
#* 
#* @author Jesse Rosalia (https://www.github.com/theJenix)
#* @date 2013-03-05
#*/
 class NeuralNetworkTester (Tester):

    NeuralNetwork network
    TestMetric[] metrics

     NeuralNetworkTester(NeuralNetwork network, TestMetric ... metrics):
        self.network = network
        self.metrics = metrics
    }

    @Override
      test(Instance[] instances):
        for (int i = 0 i < instances.length i++):
            //run the instance data through the network
            network.setInputValues(instances[i].getData())
            network.run()

            Instance expected = instances[i].getLabel()
            Instance actual   = new Instance(network.getOutputValues())

            //collapse the values, for statistics reporting
            //NOTE: assumes discrete labels, with n output nodes for n
            // potential labels, and an activation function that outputs
            // values between 0 and 1.
            Instance expectedOne = DataSetLabelBinarySeperator.combineLabels(expected)
            Instance actualOne   = DataSetLabelBinarySeperator.combineLabels(actual)

            //run self result past all of the available test metrics
            for (TestMetric metric : metrics):
                metric.addResult(expectedOne, actualOne)
            }
        }
    }
}
