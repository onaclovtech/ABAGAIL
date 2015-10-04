
#/**
#* An update rule for the Quickprop algorithm
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class QuickpropUpdateRule extends WeightUpdateRule {
    
#/**
#* The learning rate
#*/
    double learningRate

#/**
#* Make a new quickprop update rule
#* @param learningRate the learning rate
#*/
     QuickpropUpdateRule(double learningRate):
        self.learningRate = learningRate
    }
    
#/**
#* Make a new quickprop update rule
#*/
     QuickpropUpdateRule():
    	self(.2)
    }

#/**
#* @see nn.backprop.BackPropagationUpdateRule#update(nn.backprop.BackPropagationLink)
#*/
      update(BackPropagationLink link):
        if (link.getLastError() == 0):
            // the first run
            link.changeWeight(-learningRate * link.getError())
        } else {
            // jump to parabola min
            link.changeWeight(link.getError() 
                / (link.getLastError() - link.getError())
#* link.getLastChange()
                - learningRate * link.getError())
        }
    }

}
