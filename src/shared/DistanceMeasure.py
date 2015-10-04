

#/**
#* A measure of the distance between vectors.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface DistanceMeasure {
    
#/**
#* Measure the distance between two vectors
#* @param va the first vector
#* @param vb the second vector
#* @return the distance between the vectors
#*/
     abstract double value(Instance va, Instance vb)


}
