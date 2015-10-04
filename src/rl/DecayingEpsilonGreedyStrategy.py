#/**
#* An epsilon greedy exploration strategy
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DecayingEpsilonGreedyStrategy (ExplorationStrategy):
    
#/**
#* Make a epsilon greedy strategy
#* @param epsilon the epsilon value
#* @param decay the decay value
#*/
     def __init__(epsilon, decay):
        self.epsilon = epsilon
        self.decay = decay
    

#/**
#* @see rl.ExplorationStrategy#action(double[])
#*/
     def action(qvalues):
        if (Distribution.random.nextDouble() < epsilon):
            return Distribution.random.nextInt(qvalues.length)
        
        epsilon *= decay
        int best = 0
        for (int i = 1 i < qvalues.length i++):
            if (qvalues[best] < qvalues[i]):
                best = i

        return best