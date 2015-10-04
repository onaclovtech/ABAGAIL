
#/**
#* A bias node, implemented as a node
#* that refuses to feed forward values
#* or backpropagate values.  This is a little
#* wasteful since as it is used it has useless
#* links that go into it.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BackPropagationBiasNode extends BackPropagationNode {
    
#/**
#* A bias node
#* @param bias the bias value to set to
#*/
     BackPropagationBiasNode(double bias):
        super(null)
        setActivation(bias)
    }

#/**
#* @see nn.FeedForwardNode#feedforward()
#*/    
      feedforward(): }
    
#/**
#* @see nn.backprop.BackPropagationNode#backpropagate()
#*/
      backpropagate(): }
    
}
