




#/**
#* A test class for testing long term dependencies
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class HMMConditionalMonsterKnowledgeTest {
#/** The sequence count */
    static int SEQUENCE_COUNT = 5
#/** The sequence count */
    static int SEQUENCE_LENGTH = 100

#/** The state count */
    static int STATE_COUNT = 4
    
#/** The input range */
    static int INPUT_RANGE = 4
#/** The smell left input */
    static int SMELL_DAY = 0
#/** The no smell input */
    static int NO_SMELL_DAY = 1
#/** The smell left input */
    static int SMELL_NIGHT = 2
#/** The no smell input */
    static int NO_SMELL_NIGHT = 3

#/** The output range */
    static int OUTPUT_RANGE = 4
#/** The move left output */
    static int RUN_AWAY = 0
#/** The move right output */
    static int RUN_TOWARDS = 1
#/** The move up output */
    static int STAY_STILL = 2
#/** The move up output */
    static int SLEEP = 3

    
#/**
#* The main method
#* @param args ignored
#*/
     static  main(String[] args):
        int count = 0
        int goodCount = 0
        int iterations = 0
        while (count < 1000):
        // simple wumpus world test
        Distribution[] knowledge = new Distribution[] {
            // run away
            new DiscreteDistributionTable(new double[][] {
                { 1.0, 0, 0, 0},
                { 1.0, 0, 0, 0 },
                { 1.0, 0, 0, 0 },
                { 1.0, 0, 0, 0 },}),
            // run towards
            new DiscreteDistributionTable(new double[][] {
                { 0, 1.0, 0, 0 },
                { 0, 1.0, 0, 0 },
                { 0, 1.0, 0, 0 },
                { 0, 1.0, 0, 0 },}),
            // sedentary
            new DiscreteDistributionTable(new double[][] {
                { 0, 0, 1.0, 0 },
                { 0, 0, 1.0, 0 },
                { 0, 0, 0, 1.0 },
                { 0, 0, 0, 1.0 },}),
        }
        ModularHiddenMarkovModel model = new ModularHiddenMarkovModel(STATE_COUNT)
        model.setOutputDistributions(new Distribution[] {
            new FixedComponentMixtureDistribution(knowledge, DiscreteDistribution.random(knowledge.length).getProbabilities()),
            new FixedComponentMixtureDistribution(knowledge, DiscreteDistribution.random(knowledge.length).getProbabilities()),
            new FixedComponentMixtureDistribution(knowledge, DiscreteDistribution.random(knowledge.length).getProbabilities()),
            new FixedComponentMixtureDistribution(knowledge, DiscreteDistribution.random(knowledge.length).getProbabilities()),})
        model.setTransitionDistributions(new StateDistribution[] {
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),
            new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()),})
        model.setInitialStateDistribution(new SimpleStateDistributionTable(DiscreteDistributionTable.random(INPUT_RANGE, STATE_COUNT).getProbabilityMatrix()))
        Instance[][] sequences = new Instance[SEQUENCE_COUNT][]
        Random random = new Random()
        for (int i = 0 i < sequences.length i++):
            sequences[i] = new Instance[SEQUENCE_LENGTH]
            boolean smellSomething = random.nextBoolean()
            boolean day = random.nextBoolean()
            boolean isHungry = true
            double smellProbability = random.nextDouble()
            double dayProbability = random.nextDouble()
            for (int j = 0 j < sequences[i].length j++):
                if (smellSomething && isHungry):
                    if (day):
                        sequences[i][j] = new Instance(SMELL_DAY)
                        sequences[i][j].setLabel(new Instance(RUN_TOWARDS))       
                    } else {
                        sequences[i][j] = new Instance(SMELL_NIGHT)
                        sequences[i][j].setLabel(new Instance(RUN_TOWARDS))          
                    }
                } else if (smellSomething && !isHungry):
                    if (day):
                        sequences[i][j] = new Instance(SMELL_DAY)
                        sequences[i][j].setLabel(new Instance(RUN_AWAY))          
       
                    } else {
                        sequences[i][j] = new Instance(SMELL_NIGHT)
                        sequences[i][j].setLabel(new Instance(RUN_AWAY))          
     
                    }
                } else {
                    if (day):
                        sequences[i][j] = new Instance(NO_SMELL_DAY)
                        sequences[i][j].setLabel(new Instance(STAY_STILL))          
     
                    } else {
                        sequences[i][j] = new Instance(NO_SMELL_NIGHT)
                        sequences[i][j].setLabel(new Instance(SLEEP))          
    
                    }
                }
                if (random.nextDouble() < smellProbability):
                    smellProbability = random.nextDouble()
                    if (smellSomething):
                        smellSomething = false
                        isHungry = !isHungry
                    } else {
                        smellSomething = true
                    }
                }
                if (random.nextDouble() < dayProbability):
                    dayProbability = random.nextDouble()
                    day = !day
                }
            }
        }
        
        DataSet[] dataSets = new DataSet[sequences.length]
        for (int i = 0 i < dataSets.length i++):
            dataSets[i] = new DataSet(sequences[i])
        }

        System.out.println("Reestimations of model based on sequences: ")

		HiddenMarkovModelReestimator bwr = new HiddenMarkovModelReestimator(model, dataSets)
		ConvergenceTrainer trainer = new ConvergenceTrainer(bwr)
		trainer.train()
		iterations += trainer.getIterations()
        System.out.println(model + "\n")
        
        System.out.println("Log probabilities of sequences: ")
        boolean success = true
        for (int i = 0 i < sequences.length i++):
            ForwardBackwardProbabilityCalculator fbc = new ForwardBackwardProbabilityCalculator(model, dataSets[i])
            System.out.println(fbc.calculateLogProbability())
            if (success && fbc.calculateLogProbability() < -.01):
                success = false
                System.out.println("FAILURE")
            } 
            
        }
        if (success):
            goodCount++
        }
        count++
		System.out.println("So Far " + goodCount + " / " + count)
		System.out.println(iterations + " iterations")
		}
		System.out.println(goodCount + " / " + count)
		System.out.println(iterations + " iterations") 
    }
}