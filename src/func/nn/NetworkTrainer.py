#/**
# * A class that represents a trainer for
# * a neural network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class NetworkTrainer(Trainer):
    
#    /**
#     * The patterns that are being trained on
#     */
    self.patterns;
    
    /**
     * The network being trained
     */
    self.network;
    
    /**
     * The error measure to use in training
     */
    self.errorMeasure;
    
    /**
     * Make a new network trainer
     * @param patterns the patterns
     * @param network the network
     */
    def __init__(self, patterns, network, errorMeasure):
        self.patterns = patterns
        self.network = network
        self.errorMeasure = errorMeasure

#    /**
#     * Get the network
#     * @return the network
#     */
    def getNetwork(self):
        return self.network
    
#    /**
#     * Get the error measure to use when training
#     * @return the error measure
#     */
    def getErrorMeasure(self):
        return errorMeasure

#    /**
#     * Get the patterns
#     * @return the pattern
#     */
    def getDataSet(self):
        return self.patterns
