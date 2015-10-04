
#/**
#* An attribute type specifies what type an attribute
#* within a data set is
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class AttributeType {
#/**
#* The binary type
#*/
     static final AttributeType BINARY = new AttributeType(1)   
#/**
#* The integer / discrete type
#*/
     static final AttributeType DISCRETE = new AttributeType(2)
#/**
#* The continuous type
#*/
     static final AttributeType CONTINUOUS = new AttributeType(3)
    
#/**
#* The type of the attribute
#*/
    int type
    
#/**
#* Make a new attribute type
#* @param t the type of the attribute
#*/
    AttributeType(int t):
        type = t
    }
    
#/**
#* @see java.lang.Object#equals(java.lang.Object)
#*/
     boolean equals(Object o):
        return ((AttributeType) o).type == type
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        if (self == BINARY):
            return "BINARY"
        } else if (self == DISCRETE):
            return "DISCRETE"
        } else if (self == CONTINUOUS):
            return "CONTINUOUS"
        } else {
            return "UNKNOWN"
        }
    }

}
