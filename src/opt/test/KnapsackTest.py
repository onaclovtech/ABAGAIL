



#/**
#* A test of the knap sack problem
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KnapsackTest {
#/** Random number generator */
    static final Random random = new Random()
#/** The number of items */
    static final int NUM_ITEMS = 40
#/** The number of copies each */
    static final int COPIES_EACH = 4
#/** The maximum weight for a single element */
    static final double MAX_WEIGHT = 50
#/** The maximum volume for a single element */
    static final double MAX_VOLUME = 50
#/** The volume of the knapsack */
    static final double KNAPSACK_VOLUME = 
         MAX_VOLUME * NUM_ITEMS * COPIES_EACH * .4
#/**
#* The test main
#* @param args ignored
#*/
     static  main(String[] args):
        int[] copies = new int[NUM_ITEMS]
        Arrays.fill(copies, COPIES_EACH)
        double[] weights = new double[NUM_ITEMS]
        double[] volumes = new double[NUM_ITEMS]
        for (int i = 0 i < NUM_ITEMS i++):
            weights[i] = random.nextDouble() * MAX_WEIGHT
            volumes[i] = random.nextDouble() * MAX_VOLUME
        }
         int[] ranges = new int[NUM_ITEMS]
        Arrays.fill(ranges, COPIES_EACH + 1)
        EvaluationFunction ef = new KnapsackEvaluationFunction(weights, volumes, KNAPSACK_VOLUME, copies)
        Distribution odd = new DiscreteUniformDistribution(ranges)
        NeighborFunction nf = new DiscreteChangeOneNeighbor(ranges)
        MutationFunction mf = new DiscreteChangeOneMutation(ranges)
        CrossoverFunction cf = new UniformCrossOver()
        Distribution df = new DiscreteDependencyTree(.1, ranges) 
        HillClimbingProblem hcp = new GenericHillClimbingProblem(ef, odd, nf)
        GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
        ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef, odd, df)
        
        RandomizedHillClimbing rhc = new RandomizedHillClimbing(hcp)      
        FixedIterationTrainer fit = new FixedIterationTrainer(rhc, 200000)
        fit.train()
        System.out.println(ef.value(rhc.getOptimal()))
        
        SimulatedAnnealing sa = new SimulatedAnnealing(100, .95, hcp)
        fit = new FixedIterationTrainer(sa, 200000)
        fit.train()
        System.out.println(ef.value(sa.getOptimal()))
        
        StandardGeneticAlgorithm ga = new StandardGeneticAlgorithm(200, 150, 25, gap)
        fit = new FixedIterationTrainer(ga, 1000)
        fit.train()
        System.out.println(ef.value(ga.getOptimal()))
        
        MIMIC mimic = new MIMIC(200, 100, pop)
        fit = new FixedIterationTrainer(mimic, 1000)
        fit.train()
        System.out.println(ef.value(mimic.getOptimal()))
    }

}