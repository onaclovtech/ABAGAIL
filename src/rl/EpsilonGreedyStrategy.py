

#/**
#* An epsilon greedy exploration strategy
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class EpsilonGreedyStrategy (ExplorationStrategy):
#/**
#* The epsilon value
#*/
    double epsilon
    
#/**
#* Make a epsilon greedy strategy
#* @param epsilon the epsilon value
#*/
     def __init__(epsilon):
        self.epsilon = epsilon
    

#/**
#* @see rl.ExplorationStrategy#action(double[])
#*/
     def action(qvalues):
        if (Distribution.random.nextDouble() < epsilon):
            return Distribution.random.nextInt(qvalues.length)
        best = 0
        for (int i = 1 i < qvalues.length i++):
            if (qvalues[best] < qvalues[i]):
                best = i
        return best
