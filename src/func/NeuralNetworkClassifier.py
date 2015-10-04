#/**
# * A neural network classifier
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class NeuralNetworkClassifier(AbstractConditionalDistribution, FunctionApproximater):
    
#    /**
#     * The transfer function
#     */
    private DifferentiableActivationFunction activationFunction;
    
#    /**
#     * The hidden node count
#     */
    private int hiddenNodeCount;

#    /**
#     * The training weight update rule
#     */
    private WeightUpdateRule updateRule;
    
#    /**
#     * The network
#     */
    private BackPropagationNetwork network;
    
    /**
     * Make a new nn classifier
     * @param hiddenNodeCount the hidden node count
     * @param activationFunction the activation function
     * @param updateRule the update rule
     */
    def __init__(hiddenNodeCount = 3, activationFunction = new HyperbolicTangentSigmoid(), updateRule = new RPROPUpdateRule()):
        self.hiddenNodeCount = hiddenNodeCount;
        self.activationFunction = activationFunction;
        self.updateRule = updateRule
    
    /**
     * @see func.FunctionApproximater#estimate(shared.DataSet)
     */
    def estimate(self, set):
        if (set.getDescription() == null):
            set.setDescription(new DataSetDescription(set))
        int[] topology;
        if (hiddenNodeCount != 0):
            topology = new int[3]
            topology[1] = hiddenNodeCount
        else:
            topology = new int[2]
        topology[0] = set.getDescription().getAttributeTypes().length
        if (set.getDescription().getLabelDescription().getDiscreteRange() == 2):
            topology[topology.length - 1] = 1
        else:
            topology[topology.length - 1] = 
                set.getDescription().getLabelDescription().getDiscreteRange()
        network = (new BackPropagationNetworkFactory())
            .createClassificationNetwork(topology, activationFunction);
        GradientErrorMeasure errorMeasure = new SumOfSquaresError();
        Trainer trainer = new ConvergenceTrainer(
            new BatchBackPropagationTrainer(
                set, network, errorMeasure, updateRule));
        trainer.train()
    
#    /**
#     * Get a distribution for the given input
#     * @param input the input
#     * @return the distribution
#     */
    def distributionFor(self, input):
        network.setInputValues(input.getData())
        network.run()
        if (network.getOutputLayer().getNodeCount() > 1):
            return new DiscreteDistribution(
                network.getOutputValues())            
        else:
            double[] p = new double[2]
            p[1] = network.getOutputValues().get(0)
            p[0] = 1 - p[1]
            return new DiscreteDistribution(p)

#    /**
#     * @see func.FunctionApproximater#value(shared.Instance)
#     */
    def value(self, i):
        return distributionFor(i).mode()
