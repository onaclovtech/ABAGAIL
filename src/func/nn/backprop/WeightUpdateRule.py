

#/**
#* An  update rule for a back propagation link
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class WeightUpdateRule (Serializable):
    
#/**
#* Update the given link
#* @param link the link to update
#*/
     abstract  update(BackPropagationLink link)

}
