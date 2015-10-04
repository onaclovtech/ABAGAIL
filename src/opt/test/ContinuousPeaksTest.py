



#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ContinuousPeaksTest {
#/** The n value */
    static final int N = 60
#/** The t value */
    static final int T = N / 10
    
     static  main(String[] args):
        int[] ranges = new int[N]
        Arrays.fill(ranges, 2)
        EvaluationFunction ef = new ContinuousPeaksEvaluationFunction(T)
        Distribution odd = new DiscreteUniformDistribution(ranges)
        NeighborFunction nf = new DiscreteChangeOneNeighbor(ranges)
        MutationFunction mf = new DiscreteChangeOneMutation(ranges)
        CrossoverFunction cf = new SingleCrossOver()
        Distribution df = new DiscreteDependencyTree(.1, ranges) 
        HillClimbingProblem hcp = new GenericHillClimbingProblem(ef, odd, nf)
        GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
        ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef, odd, df)
        
        RandomizedHillClimbing rhc = new RandomizedHillClimbing(hcp)      
        FixedIterationTrainer fit = new FixedIterationTrainer(rhc, 200000)
        fit.train()
        System.out.println(ef.value(rhc.getOptimal()))
        
        SimulatedAnnealing sa = new SimulatedAnnealing(1E11, .95, hcp)
        fit = new FixedIterationTrainer(sa, 200000)
        fit.train()
        System.out.println(ef.value(sa.getOptimal()))
        
        StandardGeneticAlgorithm ga = new StandardGeneticAlgorithm(200, 100, 10, gap)
        fit = new FixedIterationTrainer(ga, 1000)
        fit.train()
        System.out.println(ef.value(ga.getOptimal()))
        
        MIMIC mimic = new MIMIC(200, 20, pop)
        fit = new FixedIterationTrainer(mimic, 1000)
        fit.train()
        System.out.println(ef.value(mimic.getOptimal()))
    }
}
