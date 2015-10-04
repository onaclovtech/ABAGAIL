

#/**
#* A policy learner is also a trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface PolicyLearner extends Trainer {
#/**
#* Get the best policy
#* @return the policy
#*/
     Policy getPolicy()

}
