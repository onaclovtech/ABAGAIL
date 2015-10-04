

#/**
#* A test class for running a simple wumpus world
#* example
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class HMMWumpusTest {
#/** The state count */
    static int STATE_COUNT = 2
    
#/** The input range */
    static int INPUT_RANGE = 5
#/** The smell left input */
    static int SMELL_LEFT = 0
#/** The smell right input */
    static int SMELL_RIGHT = 1
#/** The smell up input */
    static int SMELL_UP = 2
#/** The smell down input */
    static int SMELL_DOWN = 3
#/** The no smell input */
    static int NO_SMELL = 4
    
#/** The output range */
    static int OUTPUT_RANGE = 4
#/** The move left output */
    static int MOVE_LEFT = 0
#/** The move right output */
    static int MOVE_RIGHT = 1
#/** The move up output */
    static int MOVE_UP = 2
#/** The move down output */
    static int MOVE_DOWN = 3
    
#/**
#* The main method
#* @param args ignored
#*/
     static  main(String[] args):
        // simple wumpus world test
        ModularHiddenMarkovModel model = new ModularHiddenMarkovModel(STATE_COUNT)
        model.setOutputDistributions(new Distribution[] {
            DiscreteDistributionTable.random(INPUT_RANGE, OUTPUT_RANGE),
            DiscreteDistributionTable.random(INPUT_RANGE, OUTPUT_RANGE),
        })
        model.setTransitionDistributions(new StateDistribution[] {
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),
        })
        model.setInitialStateDistribution(
        new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()))
        Instance[] sequence = new Instance[] {
            new Instance(NO_SMELL, MOVE_UP), 
            new Instance(SMELL_LEFT, MOVE_RIGHT), 
            new Instance(SMELL_RIGHT, MOVE_LEFT), 
            new Instance(SMELL_UP, MOVE_DOWN), 
            new Instance(SMELL_DOWN, MOVE_UP)
        }
        DataSet[] sequences = new DataSet[] {
            new DataSet(sequence),
        }
        System.out.println(model + "\n")
        System.out.println("Observation Sequences: ")
        for (int i = 0 i < sequences.length i++):
            System.out.println(sequences[i])
        }
        System.out.println()
        ForwardBackwardProbabilityCalculator fbc = new ForwardBackwardProbabilityCalculator(model, sequences[0])
        System.out.println("Log probability of first sequence: ")
        System.out.println(fbc.calculateLogProbability())
        System.out.println()
        StateSequenceCalculator vc =new StateSequenceCalculator(model, sequences[0])
        int[] states = vc.calculateStateSequence()
        System.out.println("Most likely state sequence of first sequence: ")
        for (int i = 0 i < states.length i++):
            System.out.print(states[i] + " ")
        }
        System.out.println()
        System.out.println()
        System.out.println("Reestimations of model based on sequences: ")
        HiddenMarkovModelReestimator bwr = new HiddenMarkovModelReestimator(model, sequences)
        bwr.train()
        System.out.println(model + "\n")
        bwr.train()
        System.out.println(model + "\n")      
        for (int i = 0 i < 20 i++):
            bwr.train()     
        }
        System.out.println(model + "\n")
        fbc = new ForwardBackwardProbabilityCalculator(model, sequences[0])
        System.out.println("Log probability of first sequence: ")
        System.out.println(fbc.calculateLogProbability())
        System.out.println("Log probabilities of other sequences: ")
        for (int i = 1 i < sequences.length i++):
            fbc = new ForwardBackwardProbabilityCalculator(model, sequences[i])
            System.out.println(fbc.calculateLogProbability())
        }
            
    }
}
