
#/**
#* Very basic update rule with no momentum
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BasicUpdateRule extends WeightUpdateRule {
#/**
#* The learning rate to use
#*/
    double learningRate


#/**
#* Create a new basic update rule
#* @param learningRate the learning rate
#*/
     BasicUpdateRule(double learningRate):
        self.learningRate = learningRate            
    }
    
#/**
#* Create a new basic update rule
#*/
     BasicUpdateRule():
        self(.01)
    }

#/**
#* @see nn.backprop.BackPropagationUpdateRule#update(nn.backprop.BackPropagationLink)
#*/
      update(BackPropagationLink link):
        link.changeWeight(-learningRate * link.getError())
    }

}
