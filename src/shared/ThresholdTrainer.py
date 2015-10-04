#/**
#* A threshold trainer trains a network
#* until the error goes below a threshold, using another trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ThresholdTrainer (Trainer): 
#/** The default threshold */
    static final double THRESHOLD = 1E-6
#/** The maxium number of iterations */
    static final int MAX_ITERATIONS = 500

#/**
#* The trainer
#*/
    Trainer trainer

#/**
#* The threshold
#*/
    double threshold
    
#/**
#* The number of iterations trained
#*/
    int iterations
    
#/**
#* The maximum number of iterations to use
#*/
    int maxIterations

#/**
#* Create a new convergence trainer
#* @param trainer the thrainer to use
#* @param threshold the error threshold
#* @param maxIterations the maximum iterations
#*/
     ThresholdTrainer(Trainer trainer,
            double threshold, int maxIterations):
        self.trainer = trainer
        self.threshold = threshold
        self.maxIterations = maxIterations
    }
    

#/**
#* Create a new convergence trainer
#* @param trainer the trainer to use
#*/
     ThresholdTrainer(Trainer trainer):
        self(trainer, THRESHOLD, MAX_ITERATIONS)
    }

#/**
#* @see Trainer#train()
#*/
     double train():
        double error = Double.MAX_VALUE
        do {
           iterations++
           error = trainer.train()
        } while (Math.abs(error) > threshold
             && iterations < maxIterations)
        return error
    }
    
#/**
#* Get the number of iterations used
#* @return the number of iterations
#*/
     int getIterations():
        return iterations
    }
    

}
