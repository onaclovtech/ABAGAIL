

#/**
#* A completely greedy strategy
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class GreedyStrategy (ExplorationStrategy):


#/**
#* @see rl.ExplorationStrategy#action(double[])
#*/
     int action(double[] qvalues):
        int best = 0
        for (int i = 1 i < qvalues.length i++):
            if (qvalues[best] < qvalues[i]):
                best = i
            }
        }
        return best
    }
}
