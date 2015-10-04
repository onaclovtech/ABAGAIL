
#/**
#* An occasional printer prints out a trainer ever once in a while
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class OccasionalPrinter (Trainer):
#/**
#* The trainer being trained
#*/
    Trainer trainer
#/**
#* How many iterations to go between print
#*/
    int iterationsPerPrint
#/**
#* The current iteration
#*/
    int iteration
#/**
#* Make a new occasional printer
#* @param iterationsPerPrint the number of iterations per print
#* @param t the trainer
#*/
     OccasionalPrinter(int iterationsPerPrint, Trainer t):
        self.iterationsPerPrint = iterationsPerPrint
        self.trainer = t
    }

#/**
#* @see shared.Trainer#train()
#*/
     double train():
        if (iteration % iterationsPerPrint == 0):
            System.out.println(trainer)
        }
        iteration++
        return trainer.train()
    }

}
