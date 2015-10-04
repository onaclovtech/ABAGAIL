

#/**
#* A split in a decision tree
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class DecisionTreeSplit {

#/**
#* Get the number of branches in self split
#* @return the number of branches
#*/
     abstract int getNumberOfBranches()

#/**
#* Get the branch of the given data
#* @param d the data
#* @return the branch
#*/
     abstract int getBranchOf(Instance i)
}
