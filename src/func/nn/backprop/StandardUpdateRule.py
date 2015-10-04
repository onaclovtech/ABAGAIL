
#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class StandardUpdateRule extends WeightUpdateRule {
    
#/**
#* The learning rate to use
#*/
    double learningRate
    
#/**
#* The momentum to use
#*/
    double momentum

#/**
#* Create a new standard momentum update rule
#* @param learningRate the learning rate
#* @param momentum the momentum
#*/
     StandardUpdateRule(double learningRate, double momentum):
        self.momentum = momentum
        self.learningRate = learningRate            
    }
    
#/**
#* Create a new standard update rule
#*/
     StandardUpdateRule():
    	self(.2, .9)
    }

#/**
#* @see nn.backprop.BackPropagationUpdateRule#update(nn.backprop.BackPropagationLink)
#*/
      update(BackPropagationLink link):
        link.changeWeight(-learningRate * link.getError()
            + link.getLastChange() * momentum)
    }

}
