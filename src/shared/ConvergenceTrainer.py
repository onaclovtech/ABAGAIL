#/**
#* A convergence trainer trains a network
#* until convergence, using another trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ConvergenceTrainer (Trainer):
#/** The default threshold */
    static final double THRESHOLD = 1E-10
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
     ConvergenceTrainer(Trainer trainer,
            double threshold, int maxIterations):
        self.trainer = trainer
        self.threshold = threshold
        self.maxIterations = maxIterations
    }
    

#/**
#* Create a new convergence trainer
#* @param trainer the trainer to use
#*/
     ConvergenceTrainer(Trainer trainer):
        self(trainer, THRESHOLD, MAX_ITERATIONS)
    }

#/**
#* @see Trainer#train()
#*/
     double train():
        double lastError
        double error = Double.MAX_VALUE
        do {
           iterations++
           lastError = error
           error = trainer.train()
        } while (Math.abs(error - lastError) > threshold
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
