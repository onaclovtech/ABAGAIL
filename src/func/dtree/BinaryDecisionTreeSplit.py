

#/**
#* A standard decision tree split
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BinaryDecisionTreeSplit extends DecisionTreeSplit {
    
#/**
#* The attribute being split on
#*/
    int attribute
    
#/**
#* The splitting value
#*/
    int value
    
#/**
#* Create a new binary decision tree split
#* @param attribute the attribute being split on
#* @param value the value split on
#*/
     BinaryDecisionTreeSplit(int attribute,int value):
        self.attribute = attribute
        self.value = value
    }

#/**
#* @see dtrees.DecisionTreeSplit#getNumberOfBranches()
#*/
     int getNumberOfBranches():
        return 2
    }


#/**
#* @see dtree.DecisionTreeSplit#getBranchOf(shared.Instance)
#*/
     int getBranchOf(Instance i):
        if (i.getDiscrete(attribute) == value):
            return 0
        } else {
            return 1 
        }
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "attribute " + attribute + " == " + value
    }

}
