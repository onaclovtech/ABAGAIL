
#/**
#* A fixed iteration trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FixedIterationTrainer (Trainer):
    
#/**
#* The inner trainer
#*/
    Trainer trainer
    
#/**
#* The number of iterations to train
#*/
    int iterations
    
#/**
#* Make a new fixed iterations trainer
#* @param t the trainer
#* @param iter the number of iterations
#*/
     FixedIterationTrainer(Trainer t, int iter):
        trainer = t
        iterations = iter
    }

#/**
#* @see shared.Trainer#train()
#*/
     double train():
        double sum = 0
        for (int i = 0 i < iterations i++):
            sum += trainer.train()
        }
        return sum / iterations
    }
    

}
