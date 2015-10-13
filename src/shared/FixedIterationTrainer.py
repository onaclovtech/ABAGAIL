
#/**
#* A fixed iteration trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class FixedIterationTrainer:
    
#/**
#* The inner trainer
#*/
 #   Trainer trainer
    
#/**
#* The number of iterations to train
#*/
  #  int iterations
    
#/**
#* Make a new fixed iterations trainer
#* @param t the trainer
#* @param iter the number of iterations
#*/
     def __init__(self, t, iter):
        self.trainer = t
        self.iterations = iter
    

#/**
#* @see shared.Trainer#train()
#*/
     def train(self):
        sum = 0
        for i in  range(self.iterations):
            sum += self.trainer.train()
        return float(sum) / self.iterations