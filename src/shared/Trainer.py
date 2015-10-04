

#/**
#* An abstract trainer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface Trainer extends Serializable {
#/**
#* The train the whatever
#* @return the error
#*/
     abstract double train()
}
