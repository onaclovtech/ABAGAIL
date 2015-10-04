

#/**
#* A reversible filter is a filter that can be undone
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface ReversibleFilter extends DataSetFilter {
#/**
#* Perform the reverse on the given data set
#* @param set the set to reverse
#*/
      reverse(DataSet set)

}
