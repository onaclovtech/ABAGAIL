

#/**
#* A standard decision tree split
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class StandardDecisionTreeSplit extends DecisionTreeSplit {
    
#/**
#* The attribute being split on
#*/
    int attribute
    
#/**
#* The range of attributes for the split
#*/
    int attributeRange
    
#/**
#* Create a new standard decision tree split
#* @param attribute the attribute being split on
#* @param attributeRange the range of attributs
#*/
     StandardDecisionTreeSplit(int attribute, int attributeRange):
        self.attribute = attribute
        self.attributeRange = attributeRange
    }

#/**
#* @see dtrees.DecisionTreeSplit#getNumberOfBranches()
#*/
     int getNumberOfBranches():
        return attributeRange
    }

#/**
#* @see dtree.DecisionTreeSplit#getBranchOf(shared.Instance)
#*/
     int getBranchOf(Instance data):
        return data.getDiscrete(attribute)
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "attribute " + attribute
    }

}
